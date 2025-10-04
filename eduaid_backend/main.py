from fastapi import FastAPI
from eduaid_backend.utils import gemini, elevenlabs_api, snowflake_db

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "EduAid backend is alive!"}


@app.post("/summarize")
def summarize_endpoint(text: str):
    summary = gemini.summarize_text(text)
    snowflake_db.save_to_db({"input": text, "summary": summary})
    return {"summary": summary}


@app.post("/speak")
def speak_endpoint(text: str):
    file = elevenlabs_api.text_to_speech(text)
    return {"file": file}
