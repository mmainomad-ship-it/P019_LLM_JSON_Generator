# Project 19: JSON Data Generator

## Description
This project demonstrates how to force a Large Language Model (LLM) to generate structured data in strict JSON format. It generates a list of fictional user profiles and uses Python's `json` module to parse and validate the output, ensuring reliability for downstream applications.

## Key Features
- **Strict JSON Constraint**: Forces the LLM to output raw JSON.
- **Data Parsing**: Uses Python's `json.loads()` to convert text to objects.
- **Local AI**: Powered by local models via Ollama.
- **Validation**: Verifies data structure programmatically.

## Technology Stack
- **Python 3.x**
- **Ollama** (Local LLM Inference)
- **JSON** (Standard Library)

## Setup Instructions
1. Clone the repository.
2. Create a virtual environment: `python -m venv venv`
3. Install dependencies: `pip install -r requirements.txt`
4. Ensure Ollama is running locally.
5. Run the script: `python json_generator.py`

## Author
**mmainomad-ship-it**

## GitHub
https://github.com/mmainomad-ship-it/P019_LLM_JSON_Generator