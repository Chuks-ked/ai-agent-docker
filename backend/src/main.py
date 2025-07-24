import os
from fastapi import FastAPI

app = FastAPI()

API_KEY = os.environ.get("API_KEY")
if not API_KEY:
    raise NotImplementedError("API_KEY environment variable is not set.")

@app.get("/")
async def read_index():
    return {"message": "Welcome to the AI Agent Docker Backend!"}

