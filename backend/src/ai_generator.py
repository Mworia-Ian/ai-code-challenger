import os
import json
import requests
from typing import Dict, Any

DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
DEEPSEEK_API_URL = "https://api.deepseek.com/v1/chat/completions"

def generate_challenge(difficulty: str) -> Dict[str, Any]:
    system_prompt = """You are an expert coding challenge creator. 
    Your task is to generate a coding question with multiple choice answers.
    The question should be appropriate for the specified difficulty level.

    For easy questions: Focus on basic syntax, simple operations, or common programming concepts.
    For medium questions: Cover intermediate concepts like data structures, algorithms, or language features.
    For hard questions: Include advanced topics, design patterns, optimization techniques, or complex algorithms.

    Return the challenge in the following JSON structure:
    {
        "title": "The question title",
        "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
        "correct_answer_id": 0, // Index of the correct answer (0-3)
        "explanation": "Detailed explanation of why the correct answer is right"
    }

    Make sure the options are plausible but with only one clearly correct answer.
    """
    try:
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {DEEPSEEK_API_KEY}"
        }
        
        payload = {
            "model": "deepseek-chat",
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Generate a challenge for {difficulty} difficulty level."}
            ],
            "temperature": 0.7
        }
        
        response = requests.post(DEEPSEEK_API_URL, headers=headers, json=payload)
        response.raise_for_status()
        
        content = response.json()["choices"][0]["message"]["content"]

        # The API may return a JSON object inside a markdown code block.
        # This extracts the JSON string before parsing.
        if '```json' in content:
            json_start = content.find('{')
            json_end = content.rfind('}') + 1
            json_string = content[json_start:json_end]
            challenge_data = json.loads(json_string)
        else:
            challenge_data = json.loads(content)
        required_fields = ["title", "options", "correct_answer_id", "explanation"]
        
        for field in required_fields:
            if field not in challenge_data:
                raise ValueError(f"Missing required field: {field}")
        
        return challenge_data
        
    except Exception as e:
        print(f"An error occurred: {e}")
        return {
            "title": "Error: Could Not Generate Challenge",
            "options": ["A", "B", "C", "D"],
            "correct_answer_id": 0,
            "explanation": "The challenge could not be generated due to an API error. Please check the server logs for more details."
        }
    