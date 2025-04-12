import faiss
import numpy as np
from src.config import EMBED_DIM, INDEX_FILE, TOP_K
from src.metadata_store import load_metadata

def create_index():
    return faiss.IndexFlatL2(EMBED_DIM)

def save_index(index):
    faiss.write_index(index, INDEX_FILE)

def load_index():
    return faiss.read_index(INDEX_FILE)

def add_to_index(index, embedding):
    index.add(np.array([embedding]))

def search_index(index, query_vector, top_k=TOP_K):
    query_vector = np.array([query_vector], dtype="float32")
    D, I = index.search(query_vector, top_k)
    metadata = load_metadata()
    return [metadata[i] for i in I[0]]
