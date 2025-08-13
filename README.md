<<<<<<< HEAD

# Resume Q&A API (Auto-generated)

This project was generated from your Colab notebook to make deployment easy.

## Detected Libraries
PyPDF2, faiss, huggingface_hub, langchain, numpy, os, sentence_transformers, torch, transformers

## Potential Features Detected
{'langchain': True, 'faiss': True, 'sentence_transformers': True, 'transformers': True, 'pypdf': True, 'pdfminer': False, 'fitz': False, 'streamlit': False, 'gradio': False, 'openai': False, 'groq': False, 'huggingface_hub': True}

## Endpoints
- `GET /health` → `{"ok": true}`
- `POST /ask` with form-data fields:
  - `pdf`: resume PDF file
  - `question`: text question

## Local run
```bash
pip install -r requirements.txt
uvicorn app:app --reload
```

## Deploy (Railway/Render)
- Use `web: uvicorn app:app --host 0.0.0.0 --port $PORT` as the start command.
- Set `ALLOWED_ORIGIN=https://<your-vercel-app>.vercel.app` after you deploy the frontend.
=======
# Chat_with_Resume
>>>>>>> c373d8a453d06d96697a15482015c4b69aa661ce
