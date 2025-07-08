# llm_utils.py
import os
import json
from openai import OpenAI
from typing import Any, Dict
from dotenv import load_dotenv
from pathlib import Path

# Ensure OPENAI_API_KEY is set in your environment
env_path = Path('.') / 'key.env'
load_dotenv(dotenv_path=env_path)

def extract_data_with_llm(text: str, template_path: str) -> Dict[str, Any]:
    """Sends a prompt to the OpenAI API to extract structured data."""
    with open(template_path, 'r') as f:
        schema = json.load(f)

    client = OpenAI()

    prompt = (
        "Extract the following fields from the provided text and return a JSON object matching this schema. If data for a given field cannot be found, then keep that field blank.\n"
        f"{json.dumps(schema, indent=2)}\n\n"  
        "Text to analyze:\n" + text + "\n\n"
        "Only output valid JSON."
    )

    response = client.responses.create(
        model = "gpt-4o",
        instructions = "You are an assistant that extracts datasheet information into JSON. Accuracy is the key, and use only data provided to you. You should only respond with the contents of a valid JSON file. Do not respond with any other text.",
        input = prompt,
    )

    return response.output_text