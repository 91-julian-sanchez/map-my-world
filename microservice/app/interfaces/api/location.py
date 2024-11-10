from app.application.create_location import create_location
from app.application.get_locations import get_locations
from app.domain.schemas.location import LocationCreate
from app.infrastructure.db import get_session
from app.infrastructure.models import Location
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel.ext.asyncio.session import AsyncSession

router = APIRouter()


@router.get("/locations", response_model=list[Location])
async def get_locations_endpoint(session: AsyncSession = Depends(get_session)):
    try:
        locations = await get_locations(session)
        return [
            Location(
                name=location.name,
                latitude=location.latitude,
                longitude=location.longitude,
            )
            for location in locations
        ]
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/locations")
async def add_location(
    location: LocationCreate, session: AsyncSession = Depends(get_session)
):
    try:
        location_model = Location(
            name=location.name, latitude=location.latitude, longitude=location.longitude
        )
        location_created = await create_location(session, location_model)
        return {"status": "success", "location": location_created}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
