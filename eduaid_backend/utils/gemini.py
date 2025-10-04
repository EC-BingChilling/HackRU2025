import os
from dotenv import load_dotenv

load_dotenv("api.env")

gemini_key = os.getenv("GEMINI_API_KEY")


def summarize_text(text: str) -> str:
    if not gemini_key:
        return "No Gemini key configured"
    try:
        from google import genai

        client = genai.Client(api_key=gemini_key)
        resp = client.models.generate_content(model="gemini-2.5-flash", contents=text)
        return resp.text
    except Exception as e:
        print("Gemini error:", e)
        return f"Error: {e}"
