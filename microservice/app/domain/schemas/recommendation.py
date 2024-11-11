from datetime import datetime

from app.domain.schemas.category import CategoryResponse
from app.domain.schemas.location import LocationResponse
from pydantic import BaseModel


class RecommendationReviewCreate(BaseModel):
    location_id: int
    category_id: int


class RecommendationReviewResponse(BaseModel):
    id: int
    location: LocationResponse
    category: CategoryResponse
    reviewed_at: datetime

    class Config:
        orm_mode = True


class Location(BaseModel):
    id: int
    name: str


class Category(BaseModel):
    id: int
    name: str


class RecommendationsNotReviewedResponse(BaseModel):
    location: Location
    category: Category
