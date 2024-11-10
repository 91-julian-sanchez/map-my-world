import os

from pydantic import BaseSettings


class Settings(BaseSettings):
    database_url: str = os.getenv("DATABASE_URL")
    app_name: str = os.getenv("APP_NAME")

    class Config:
        env_file = "./.env"


settings = Settings()
