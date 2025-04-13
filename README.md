# ByteVerse_BugOff
ByteVerse 7.0

Legal Case Analyzer: A Legal Case Query Answering System

Project Overview

## Features

### 1. **Legal Query Answering**:
- Input a legal question, and the system provides a detailed answer by retrieving relevant context from past legal judgments and providing an AI-generated response.

### 2. **Text Simplification**:
- Convert complex legal jargon into plain language to make legal text accessible to non-experts.

### 3. **Legal Dictionary**:
- Upload your document and hover over any word to decipher its meaning.

### 4. **Fast API Backend & Streamlit Frontend**:
- **FastAPI** is used for the backend to handle API requests for predictions and querying.
- **Streamlit** is used for the frontend to provide an interactive web interface for users.

## Tech Stack

- **Backend**: FastAPI
- **Frontend**: Streamlit
- **Search Engine**: FAISS (used for fast similarity search in large legal document datasets)
- **Machine Learning**: InLegalBERT for embedding generation and Mistral API for generating responses.
- **Environment Variables**: `.env` file for storing sensitive keys and configurations.
