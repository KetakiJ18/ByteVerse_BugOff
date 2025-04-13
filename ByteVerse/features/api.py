from fastapi import FastAPI
from pydantic import BaseModel
from features.interpret import explain_sentence
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins, you can specify domains like ["http://localhost:5500"]
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, PUT, DELETE)
    allow_headers=["*"],  # Allows all headers
)
class SentenceInput(BaseModel):
    sentence: str

@app.post("/simplify")  # This should be POST, not GET
def simplify(input: SentenceInput):
    explanation = explain_sentence(input.sentence)
    print(f"Explanation: {explanation}")
    return {"explanation": explanation}
