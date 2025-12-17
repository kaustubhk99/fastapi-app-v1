
from fastapi import FastAPI

app = FastAPI(title="FastAPI on Render", version="0.1.0")

@app.get("/")
async def root():
    return {"message": "Hello from FastAPI on Render!"}

@app.get("/healthz")
async def healthz():
    return {"status": "ok"}
