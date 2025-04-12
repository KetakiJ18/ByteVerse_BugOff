import os
import requests
import pandas as pd

def download_pdf(url, download_folder):
    try:
        response = requests.get(url)
        response.raise_for_status()  
        filename = os.path.join(download_folder, url.split("/")[-1])  
        with open(filename, 'wb') as file:
            file.write(response.content)
        print(f"Downloaded: {filename}")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading {url}: {e}")

def download_pdfs_from_dataset(csv_file, download_folder, pdf_column='pdf_link'):
    try:
        df = pd.read_csv(csv_file)
        print(f"Loaded dataset: {csv_file}")
        
        if pdf_column not in df.columns:
            print(f"Error: Column '{pdf_column}' not found in the dataset.")
            return
        
        if not os.path.exists(download_folder):
            os.makedirs(download_folder)
        
        for index, row in df.iterrows():
            pdf_url = row[pdf_column]
            if isinstance(pdf_url, str) and pdf_url.endswith('.pdf'):
                download_pdf(pdf_url, download_folder)
            else:
                print(f"Skipping row {index} as the URL is not a valid PDF: {pdf_url}")
                
    except Exception as e:
        print(f"Error processing the dataset: {e}")

def main():
    csv_file = input("Enter the path to your Kaggle dataset (CSV): ")
    download_folder = input("Enter the folder where PDFs should be saved: ")
    
    download_pdfs_from_dataset(csv_file, download_folder)

if __name__ == '__main__':
    main()