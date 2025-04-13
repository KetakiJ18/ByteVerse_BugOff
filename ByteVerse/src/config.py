PDF_DIR = "./data/"
INDEX_FILE = "legal_index.faiss"
META_FILE = "metadata.json"
DEVICE = "cuda" if __import__("torch").cuda.is_available() else "cpu"
EMBED_DIM = 768
TOP_K = 5