
# FastAPI on Render

Minimal FastAPI app ready to deploy on Render.

## Local run

python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000

# Visit:
# http://localhost:8000 and http://localhost:8000/docs

## Deploy to Render

1. Push this repo to GitHub/GitLab/Bitbucket.
2. In Render, create a Web Service and connect the repo.
3. Use:
   - Build Command: pip install -r requirements.txt
   - Start Command: uvicorn main:app --host 0.0.0.0 --port $PORT
