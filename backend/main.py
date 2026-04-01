from fastapi import FastAPI
from backend.api.routes import router   # <-- IMPORTANT FIX

app = FastAPI()   # <-- THIS must exist

app.include_router(router)

@app.get("/")
def root():
    return {"message": "AI Ops Running"}