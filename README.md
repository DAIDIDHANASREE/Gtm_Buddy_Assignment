# Gtm_Buddy_Assignment
# Flask API Project for Multi-Label Classification and NER

## Project Overview
This project provides a REST API for:
- **Multi-label classification** of input text snippets.
- **Named Entity Recognition (NER)** using spaCy.
- **Text Summarization** for concise overviews.

## Repository Structure

## Setup Instructions

### Prerequisites
- Python 3.9+
- Docker (for containerization)

### Steps to Run Locally
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd flask_api_project_static
pip install -r requirements.txt
python -m spacy download en_core_web_sm
python app.py
### Steps to Run with Docker
docker build -t flask_static_api 
docker run -p 5000:5000 flask_static_api


