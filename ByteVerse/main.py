import os
from tqdm import tqdm
from src.config import PDF_DIR
from src.embedder import extract_text, get_embedding
from src.faiss_indexer import create_index, add_to_index, save_index, search_index
from src.metadata_store import save_metadata

def build_index():
    from src.config import INDEX_FILE, META_FILE

    index = create_index()
    metadata_store = []
    print(f"PDF Directory: {PDF_DIR}")
    pdf_files = [f for f in os.listdir(PDF_DIR) if f.endswith(".pdf")]
    print(f"Found {len(pdf_files)} PDFs.")

    for fname in tqdm(pdf_files, desc="Indexing PDFs"):
        path = os.path.join(PDF_DIR, fname)
        try:
            text = extract_text(path)
            print(f"Extracted text from {fname}: {text[:500]}")
            if not text: continue
            embedding = get_embedding(text)
            print(f"Generated embedding for {fname}: {embedding[:5]}...")
            add_to_index(index, embedding)

            metadata_store.append({
                "file_name": fname,
                "file_path": path,
                "text_snippet": text[:500]
            })

        except Exception as e:
            print(f"⚠️ Failed: {fname} — {e}")

    save_index(index)
    save_metadata(metadata_store)
    print(f"✅ Indexed {len(metadata_store)} documents.")

def query_example():
    from src.faiss_indexer import load_index, search_index
    from src.embedder import get_embedding

    index = load_index()

    query_text = input("\n🔍 Enter a case description to search: ")
    query_vec = get_embedding(query_text)

    results = search_index(index, query_vec)

    print("\n🔗 Top matches:")
    for r in results:
        print(f"📄 {r['file_name']}\n   ➤ {r['text_snippet'][:200]}...\n")

if __name__ == "__main__":
    print("📦 1. Building FAISS Index")
    build_index()

    print("\n🔎 2. Example Query")
    query_example()
