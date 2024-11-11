from app.core.config import settings

DATABASE_URL = f"postgresql+asyncpg://{settings.postgres_user}:{settings.postgres_password}@db:{settings.postgres_port}/{settings.postgres_db}"  # noqa: E501
