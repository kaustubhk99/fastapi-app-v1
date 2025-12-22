from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pathlib import Path
import os

app = FastAPI(title="FastAPI on Render", version="0.1.0")

# API Routes - all under /api prefix
@app.get("/api")
async def root():
    return {
        "message": "Hello from FastAPI on Render!",
        "status": "success",
        "version": "1.0.0"
    }

@app.get("/api/healthz")
async def healthz():
    return {"status": "ok"}

@app.get("/api/data")
async def get_data():
    """Example API endpoint - add your logic here"""
    return {
        "items": ["item1", "item2", "item3"],
        "count": 3,
        "message": "Data retrieved successfully"
    }

# Serve static files
frontend_path = Path(__file__).parent / "frontend"

# Mount static assets (CSS, JS)
if frontend_path.exists():
    app.mount("/assets", StaticFiles(directory=frontend_path), name="assets")

# Serve index.html for root and all non-API routes
@app.get("/{full_path:path}")
async def serve_frontend(full_path: str):
    # Don't serve frontend for API routes
    if full_path.startswith("api/"):
        return {"error": "API endpoint not found"}, 404
    
    # Serve index.html for all other routes
    index_file = frontend_path / "index.html"
    if index_file.exists():
        return FileResponse(index_file)
    return {"error": "Frontend not found"}, 404