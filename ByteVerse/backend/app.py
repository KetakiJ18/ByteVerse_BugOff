from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import json
import os
from dotenv import load_dotenv
import httpx
import re

load_dotenv()

app = FastAPI()

class Query(BaseModel):
    text: str

embedder = SentenceTransformer("law-ai/InLegalBERT")

index = faiss.read_index("legal_index.faiss")
print("✅ FAISS index loaded")
print("FAISS index dimension:", index.d)

with open("metadata.json", "r") as f:
    metadata = json.load(f)

MISTRAL_API_URL = "https://api.mistral.ai/v1/chat/completions"
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")

HEADERS = {
    "Authorization": f"Bearer {MISTRAL_API_KEY}",
    "Content-Type": "application/json"
}

async def generate_rag_response(query):
    query_embedding = embedder.encode(query, convert_to_numpy=True).astype("float32")
    if len(query_embedding.shape) == 1:
        query_embedding = np.expand_dims(query_embedding, axis=0)

    D, I = index.search(query_embedding, k=3)

    retrieved_docs = []
    for i in I[0]:
        doc = metadata[i].get("content", "") if isinstance(metadata[i], dict) else metadata[i]
        retrieved_docs.append(doc)

    context = "\n\n".join([metadata[i]['content'] for i in I[0] if i < len(metadata)])

    print("\n🧾 Retrieved Context:\n" + "-"*40)
    print(context)
    print("-"*40 + "\n")

    messages = [
        {"role": "system", "content": "You are a legal assistant who answers based on the given context."},
        {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {query}"}
    ]

    payload = {
        "model": "mistral-small",
        "messages": messages,
        "temperature": 0.7,
        "top_p": 0.9,
        "max_tokens": 300
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(MISTRAL_API_URL, headers=HEADERS, json=payload)

    if response.status_code == 200:
        ai_response = response.json()["choices"][0]["message"]["content"].strip()
        return ai_response
    else:
        return f"❌ Error from Mistral API: {response.status_code} - {response.text}"


def format_response(ai_response):
    cleaned_response = "\n".join([line.strip() for line in ai_response.strip().split("\n") if line.strip()])
    
    paragraphs = cleaned_response.split("\n")

    formatted_response = "\n\n".join(paragraphs)

    return formatted_response


@app.post("/predict/")
async def predict(request: Request):
    data = await request.json()

    ai_response = await generate_rag_response(data["text"])

    formatted_response = format_response(ai_response)

    return JSONResponse(content={"response": formatted_response})
