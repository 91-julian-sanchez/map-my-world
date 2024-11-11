from typing import List

from app.application.create_location import create_location
from app.application.get_locations import get_locations
from app.domain.schemas.location import LocationCreate
from app.domain.schemas.recommendation import LocationResponse
from app.infrastructure.db import get_session
from app.infrastructure.models import Location
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel.ext.asyncio.session import AsyncSession

router = APIRouter()


@router.get(
    "/locations",
    response_model=List[LocationResponse],
    summary="Retrieve Locations",
    description="Get a list of all locations.",
    tags=["Locations"],
)
async def get_locations_endpoint(session: AsyncSession = Depends(get_session)):
    """
    Endpoint to retrieve all locations from the database.
    - **session**: Database session dependency for accessing the database.
    """
    try:
        return await get_locations(session)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post(
    "/locations",
    response_model=LocationResponse,
    summary="Add a New Location",
    description="Create a new location.",
    tags=["Locations"],
)
async def add_location_endpoint(
    location: LocationCreate, session: AsyncSession = Depends(get_session)
):
    """
    Endpoint to add a new location to the database.
    - **location**: Data for the new location including name, latitude, and longitude.
    - **session**: Database session dependency for accessing the database.
    """
    try:
        location_model = Location(
            name=location.name, latitude=location.latitude, longitude=location.longitude
        )
        return await create_location(session, location_model)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
