import os

from pydantic import BaseSettings


class Settings(BaseSettings):
    database_url: str = os.getenv("DATABASE_URL")
    app_name: str = os.getenv("APP_NAME")
    days_since_last_review: str = os.getenv("DAYS_SINCE_LAST_REVIEW")

    class Config:
        env_file = "./.env"


settings = Settings()
