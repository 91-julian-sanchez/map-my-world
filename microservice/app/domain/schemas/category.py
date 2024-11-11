from datetime import datetime

from pydantic import BaseModel


class CategoryCreate(BaseModel):
    name: str


class CategoryResponse(BaseModel):
    id: int
    name: str
    created_at: datetime
