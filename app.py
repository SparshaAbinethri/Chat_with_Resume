# app.py
import os
from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from inference import extract_text_from_pdf, answer_question

app = FastAPI(title="Resume Q&A API", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.getenv("ALLOWED_ORIGIN", "*")],
    allow_credentials=True, allow_methods=["*"], allow_headers=["*"],
)

@app.get("/health")
def health():
    return {"ok": True}

@app.post("/ask")
async def ask(question: str = Form(...), pdf: UploadFile = File(...)):
    pdf_bytes = await pdf.read()
    context_text = extract_text_from_pdf(pdf_bytes)
    result = answer_question(question, context_text)
    return result