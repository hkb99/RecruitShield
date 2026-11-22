# RecruitShield

RecruitShield is an AI recruitment scam detection assistant for the COMP5610 
term project

## Requirements

- Python 3.11
- Google Gemini API Key


## Features

- Analyzes recruiter messgages for signs of potential fraud attempt
- Investigates sender email domains using DNS
- Generates a report including concern level and recommended next steps
- Streamlit web interface

## Setup

After cloning the repository, create a virtual environment:

```bash
cd RecruitShield
python3.11 -m venv .venv
source .venv/bin/activate
```

Install all dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file containing a Gemini API Key:

```text
GEMINI_API_KEY=your_api_key
```

## Running the application

```bash
python -m streamlit run hireapp.py
```
