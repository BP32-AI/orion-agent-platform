# app/main.py

from fastapi import FastAPI

from app.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME
)


@app.get("/")
async def root():
    return {
        "message": "Orion Agent Platform Running"
    }