from datetime import datetime, timezone
from typing import List, Optional

from sqlalchemy import UniqueConstraint
from sqlalchemy.sql import func
from sqlmodel import Field, Relationship, SQLModel


class Base(SQLModel):
    pass


class Location(Base, table=True):
    __tablename__ = "locations"
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    latitude: float = Field(nullable=False)
    longitude: float = Field(nullable=False)
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc).replace(tzinfo=None)
    )
    updated_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc).replace(tzinfo=None),
        sa_column_kwargs={"onupdate": func.now()},
    )

    reviews: List["RecommendationReview"] = Relationship(back_populates="location")

    __table_args__ = (
        UniqueConstraint("latitude", "longitude", name="uix_location_lat_long"),
    )


class Category(Base, table=True):
    __tablename__ = "categories"
    id: int = Field(default=None, primary_key=True)
    name: str
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc).replace(tzinfo=None)
    )
    updated_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc).replace(tzinfo=None),
        sa_column_kwargs={"onupdate": func.now()},
    )

    reviews: List["RecommendationReview"] = Relationship(back_populates="category")

    __table_args__ = (UniqueConstraint("name", name="uix_category_name"),)


class RecommendationReview(Base, table=True):
    __tablename__ = "location_category_reviewed"

    id: int = Field(default=None, primary_key=True)
    location_id: int = Field(foreign_key="locations.id")
    category_id: int = Field(foreign_key="categories.id")
    reviewed_at: datetime = Field(default_factory=datetime.utcnow)
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc).replace(tzinfo=None)
    )
    updated_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc).replace(tzinfo=None),
        sa_column_kwargs={"onupdate": func.now()},
    )

    location: Optional[Location] = Relationship(back_populates="reviews")
    category: Optional[Category] = Relationship(back_populates="reviews")
