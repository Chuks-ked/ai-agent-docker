from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_index():
    return {"message": "Welcome to the AI Agent Docker Backend!"}

