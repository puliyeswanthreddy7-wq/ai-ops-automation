from fastapi import APIRouter
from backend.services.pipeline import run_pipeline
from backend.services.ai_agent import ask_ai

router = APIRouter()

@router.get("/run")
def run():
    return run_pipeline()

@router.get("/ask")
def ask(q: str):
    return {"response": ask_ai(q)}