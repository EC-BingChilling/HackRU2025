from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = Fastapi(name="EduAidMVP")


class InputText(BaseModel):
    text: str


class HistoryItem(BaseModel):
    input: str
    summary: str


# very simple in-memory store
history: List[HistoryItem] = []


@app.get("/")
def root():
    return {"status": "OK", "message": "EduAid MVP Backend"}


@app.post("/summarize")
def summarize(inp: InputText):
    # 👇 placeholder summarization logic
    s = inp.text[:100] + ("…" if len(inp.text) > 100 else "")
    # Add to history
    history.append(HistoryItem(input=inp.text, summary=s))
    return {"summary": s}


@app.get("/history", response_model=List[HistoryItem])
def get_history():
    return history