from pydantic import BaseModel


class RecommendationReviewCreate(BaseModel):
    location_id: int
    category_id: int
