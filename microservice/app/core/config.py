import os

from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = os.getenv("APP_NAME")
    postgres_user: str = os.getenv("POSTGRES_USER")
    postgres_password: str = os.getenv("POSTGRES_PASSWORD")
    postgres_port: str = os.getenv("POSTGRES_PORT")
    postgres_db: str = os.getenv("POSTGRES_DB")
    days_since_last_review: str = os.getenv("DAYS_SINCE_LAST_REVIEW")

    class Config:
        env_file = "./.env"


settings = Settings()
