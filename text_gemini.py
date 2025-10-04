import os
import requests
from dotenv import load_dotenv

## load from api file
load_dotenv("api.env")

gemini_key = os.getenv("GEMINI_API_KEY")
eleven_key = os.getenv("ELEVENLABS_API_KEY")

if gemini_key:
    print("success:", gemini_key[:8] + "...")
else:
    print("L")
if eleven_key:
    print("succ", eleven_key[:8] + "...")
else:
    print("L")
