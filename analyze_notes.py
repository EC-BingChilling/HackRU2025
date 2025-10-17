import os 
import json
import requests
from flask import Flask, request, jsonify
from dotenv import load_dotenv

load_dotenv("api.env")

app = Flask(__name__)

# API KEYS ---#

GEMINI_KEY = os.environ.get("GEMINI_API_KEY")
if not GEMINI_KEY:
    raise ValueError("GEMINI_API_KEY not found")
ELEVEN_KEY = os.environ.get("ELEVENLABS_API_KEY")
if not ELEVEN_KEY:
    raise ValueError("ELEVENLABS_API_KEY not found")
    
def build_gemini_prompt(notes: str) -> str:
    return (
        "Turn tjese lecture notes into 5 flashcards and 3 quiz questions in JSON format. \n"
        f"lecutre notes: {notes}\n"
        "JSON formate example: \n" 
        "{\n"
        "   'flashcards': [\n"
        "      {'question': '...', 'answer': '...'}\n"
        "  ],\n"
        "  'quiz': [\n"
        "    {'question': '...', 'options': ['A','B','C','D'], 'answer': '...'}\n"
        "  ]\n"
        "}"
    )
def query_gemini(notes: str) -> dict:
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent"
    headers = {"Authorization": f"Bearer {GEMINI_KEY}", "Content-Type": "application/json"}
    params = {"key": GEMINI_KEY}
    data = {
        "content": [{"parts": [{"text": build_gemini_prompt(notes)}]}]
    }
    
    response = requests.post(url, headers=headers, params=params, json=data)
    
    if response.status_code != 200:
        raise Exception(f"Gemini API ERROR: {response.status_code} {response.text}")
    
    try:
        text_output = response.json()["candidates"][0]["content"]["parts"]
        return json.loads(text_output) if text_output.strip().startswith("{") else {"raw": text_output}
    except Exception as e:
        raise Exception(f"failed to parse Gemini response: {e}")

#text to speach using elevenlabs 
def generate_audio(text: str) -> str:
    """convert text to speech using elevenLabs. """
    voice_id = "21m00Tcm4TlvDq8ikWAM"
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    headers = {"xi-api-key": ELEVEN_KEY, "Content-Type": "application/json"}
    data = {
        "text": text,
        "voice_setting": {"stability": 0.4, "similartiy_boost": 0.8}
    }
    
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code != 200:
        raise Exception(f"ElevenLabs API error: {response.status_code} {response.text}")
    
    audio_filename = "summary.mp3"
    with open(audio_filename, "wb") as f:
        f.write(response.content)
        
    return audio_filename
@app.route("/analyze", methods=["POST"])
def analyze_notes(): 
    payload = request.json
    notes = payload.get("notes", "").strip() if payload else ""
    
    if not notes:
        return jsonify({"error": "no notes provided"}), 400
    
    try:
        #gemini get flashcards + quiz
        gemini_result = query_gemini(notes)
        
        #optinonal: generate audio summ from notes
        
        audio_file = generate_audio(notes[:250])
        
        return jsonify({
            "flashcards_quiz": gemini_result,
            "audio_summary_file": audio_file
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# run server
if __name__ == "__main__":
    app.run(debug=True)
        
