import requests
import os

from dotenv import load_dotenv

load_dotenv()


OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

def generate_smart_caption(description: str):

    prompt = f"""
    Image description: {description}

    Generate:
    - 3 creative Instagram captions
    - Add emojis
    - Add 6 relevant hashtags
    - Do NOT use markdown.
    - Do NOT use ** or headings.
    - Return plain text only.
    - do number the captions, but do NOT number the hashtags.
    """

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "deepseek/deepseek-chat",
            "messages": [
                {"role": "user", "content": prompt}
            ]
        }
    )

    print(response.json())

    return response.json()["choices"][0]["message"]["content"]