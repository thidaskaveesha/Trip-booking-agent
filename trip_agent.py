import os
import requests
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"

def interpret_trip_request(prompt: str) -> dict:
    system_msg = "You are a travel assistant. Extract only the destination, duration (in days), and budget in LKR. Respond in valid JSON format like: {\"destination\": \"Ella\", \"duration_days\": 2, \"budget_lkr\": 30000}"

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "llama3-70b-8192",  # Or "llama3-70b-8192"
        "messages": [
            {"role": "system", "content": system_msg},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.2
    }

    response = requests.post(GROQ_URL, headers=headers, json=data)

    if response.status_code != 200:
        print("❌ Groq API error:", response.text)
        return {}

    content = response.json()["choices"][0]["message"]["content"]

    try:
        return eval(content)  # you can use json.loads(content) if needed
    except:
        return {}
