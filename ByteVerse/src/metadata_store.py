import json
from src.config import META_FILE

def save_metadata(metadata_list):
    with open(META_FILE, "w") as f:
        json.dump(metadata_list, f)

def load_metadata():
    with open(META_FILE, "r") as f:
        return json.load(f)
