import fitz  
import torch
from transformers import AutoTokenizer, AutoModel
from src.config import DEVICE

tokenizer = AutoTokenizer.from_pretrained("law-ai/InLegalBERT")
model = AutoModel.from_pretrained("law-ai/InLegalBERT").to(DEVICE)
model.eval()

def extract_text(pdf_path):
    doc = fitz.open(pdf_path)
    text = " ".join([page.get_text() for page in doc])
    doc.close()
    return text.strip()

def get_embedding(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512).to(DEVICE)
    with torch.no_grad():
        outputs = model(**inputs)
        embedding = outputs.last_hidden_state.mean(dim=1).squeeze().cpu().numpy()
    return embedding.astype("float32")
