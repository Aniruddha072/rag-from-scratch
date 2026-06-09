from fastapi import FastAPI
from pydantic import BaseModel
from src.rag.pipeline import run_pipeline

app = FastAPI()


class QuestionRequest(BaseModel):
    question: str


@app.get("/")
def home():
    return {
        "message": "RAG API is running"
    }


@app.post("/ask")
def ask_question(request: QuestionRequest):

    answer = run_pipeline(
        request.question
    )

    return {
        "answer": answer
    }