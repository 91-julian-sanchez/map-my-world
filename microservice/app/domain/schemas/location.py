from datetime import datetime

from pydantic import BaseModel


class LocationCreate(BaseModel):
    name: str
    latitude: float
    longitude: float


class LocationResponse(BaseModel):
    id: int
    name: str
    latitude: float
    longitude: float
    created_at: datetime
