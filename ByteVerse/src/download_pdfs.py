import os
import requests
import pandas as pd
from urllib.parse import urlparse
from concurrent.futures import ThreadPoolExecutor, as_completed

CSV_FILE = r'C:\Users\ketak\OneDrive\Desktop\ByteVerse\data\judgments.csv'
PDF_DIR = r'C:\Users\ketak\OneDrive\Desktop\ByteVerse\data\cases'
BASE_URL = 'https://api.sci.gov.in/'

# Max number of parallel threads
MAX_THREADS = 10

def download_pdf(file_url, save_dir):
    if not urlparse(file_url).scheme:
        file_url = BASE_URL + file_url.lstrip('/')

    file_name = os.path.basename(file_url)
    save_path = os.path.join(save_dir, file_name)

    try:
        response = requests.get(file_url, stream=True, timeout=15)
        response.raise_for_status()
        with open(save_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024):
                f.write(chunk)
        print(f"Downloaded: {file_name}")
    except Exception as e:
        print(f"❌ Failed to download {file_name}: {e}")

def download_all(csv_file, save_dir):
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    df = pd.read_csv(csv_file)
    if 'temp_link' not in df.columns:
        print("CSV missing 'temp_link' column.")
        return

    urls = df['temp_link'].dropna().tolist()

    with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        futures = [executor.submit(download_pdf, url, save_dir) for url in urls]
        for _ in as_completed(futures):
            pass  # Just waiting for all to complete

# Start download
download_all(CSV_FILE, PDF_DIR)
