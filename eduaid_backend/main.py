from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
from eduaid_backend.utils import gemini, elevenlabs_api, snowflake_db

app = FastAPI()

# ------ CORS configuration ------
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    # Add your frontend deployed URL(s) here later
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ------ Endpoints ------


@app.get("/")
def read_root():
    return {"message": "EduAid backend is alive!"}


@app.post("/summarize")
def summarize_endpoint(text: str):
    if not text or text.strip() == "":
        raise HTTPException(
            status_code=400, detail="Text parameter is required and cannot be empty"
        )
    summary = gemini.summarize_text(text)
    # Attempt to save to Snowflake
    try:
        conn = snowflake_db.get_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO summaries (input_text, summary_text) VALUES (%s, %s)",
            (text, summary),
        )
        cur.close()
        conn.close()
    except Exception as e:
        # Log the error, but don’t break the response
        print("Failed saving summary:", e)
    return {"summary": summary}


@app.post("/speak")
def speak_endpoint(text: str):
    if not text or text.strip() == "":
        raise HTTPException(
            status_code=400, detail="Text parameter is required and cannot be empty"
        )
    try:
        file_path = elevenlabs_api.text_to_speech(text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Text to speech failed: {e}")
    return {"file": file_path}


@app.get("/history")
def history_endpoint(limit: Optional[int] = 10):
    if limit is None or limit <= 0:
        raise HTTPException(status_code=400, detail="Limit must be a positive integer")
    try:
        records = snowflake_db.fetch_history(limit)
        return {"history": records}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Could not fetch history: {e}")


# You can add more endpoints as needed below
