# app/core/config.py

from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    PROJECT_NAME: str
    API_V1_STR: str

    DATABASE_URL: str
    REDIS_URL: str

    GOOGLE_API_KEY: str
    TELEGRAM_BOT_TOKEN: str

    class Config:
        env_file = ".env"


@lru_cache()
def get_settings():
    return Settings()


settings = get_settings()