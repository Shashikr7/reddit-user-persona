import httpx
import os
from dotenv import load_dotenv

load_dotenv()

TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")

def build_persona(posts, comments):
    text = "\n".join(
        [f"Post: {p[0]} {p[1]}" for p in posts] +
        [f"Comment: {c}" for c in comments]
    )

    prompt = f"""
    Based on the following Reddit posts and comments, generate a user persona that includes:
    - Interests
    - Values
    - Personality traits
    - Tone of writing
    - Likely age group
    - Possible profession

    For each trait, cite the specific post/comment that supports it.

    Text:
    {text[:12000]}
    """

    url = "https://api.together.xyz/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {TOGETHER_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "mistralai/Mixtral-8x7B-Instruct-v0.1",
        "messages": [
            {"role": "system", "content": "You are a helpful persona analyst."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7,
        "max_tokens": 1000
    }

    response = httpx.post(url, headers=headers, json=data, timeout=60)

    result = response.json()

    return result["choices"][0]["message"]["content"]
