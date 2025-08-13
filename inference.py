# inference.py
# Auto-generated from your notebook structure. Replace stubbed parts with your actual model logic.

import io
from typing import List, Tuple

try:
    from PyPDF2 import PdfReader
    HAVE_PYPDF2 = True
except Exception:
    HAVE_PYPDF2 = False

def extract_text_from_pdf(file_bytes: bytes) -> str:
    """Extract raw text from a PDF file (bytes)."""
    if HAVE_PYPDF2:
        reader = PdfReader(io.BytesIO(file_bytes))
        return "\n".join((page.extract_text() or "") for page in reader.pages)
    else:
        # Fallback naive decode if PyPDF2 isn't available
        return ""

def simple_retrieval_chunks(text: str, chunk_size: int = 800, overlap: int = 150) -> List[str]:
    """Split text into overlapping chunks for naive retrieval."""
    chunks = []
    i = 0
    while i < len(text):
        chunk = text[i:i+chunk_size]
        chunks.append(chunk)
        i += (chunk_size - overlap)
    return chunks

def naive_answer(question: str, chunks: List[str]) -> Tuple[str, float, str]:
    """Very naive matching: pick the chunk with most keyword overlap."""
    q_words = set([w.lower() for w in question.split() if len(w) > 2])
    best, score, best_chunk = "I need a better model or more context.", 0, ""
    for ch in chunks:
        words = set([w.lower() for w in ch.split() if len(w) > 2])
        s = len(q_words & words)
        if s > score:
            score, best_chunk = s, ch
            best = ch[:600]
    confidence = min(0.95, 0.2 + 0.1 * score)
    return best, confidence, best_chunk

def answer_question(question: str, context_text: str) -> dict:
    """Main entrypoint. Swap this with your vector DB + LLM pipeline."""
    chunks = simple_retrieval_chunks(context_text)
    ans, conf, ctx = naive_answer(question, chunks)
    return {
        "answer": ans,
        "confidence": round(conf, 2),
        "context_snippet": ctx[:600]
    }