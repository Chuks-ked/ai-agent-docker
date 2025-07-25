import os
from contextlib import asynccontextmanager
from fastapi import FastAPI

from api.db import init_db
from api.chat.routing import router as chat_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(chat_router, prefix="/api/chats")

API_KEY = os.environ.get("API_KEY")
if not API_KEY:
    raise NotImplementedError("API_KEY environment variable is not set.")

@app.get("/")
def read_index():
    return {"message": "Welcome to the AI Agent Docker Backend!"}

