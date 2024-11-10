from datetime import datetime, timezone
from typing import Optional

from sqlalchemy.sql import func
from sqlmodel import Field, SQLModel


class Base(SQLModel):
    pass


class Location(Base, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    latitude: float = Field(nullable=False)
    longitude: float = Field(nullable=False)
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
        .astimezone(timezone.utc)
        .replace(tzinfo=None)
    )
    updated_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
        .astimezone(timezone.utc)
        .replace(tzinfo=None),
        sa_column_kwargs={"onupdate": func.now()},
    )
