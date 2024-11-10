from typing import List, Optional

from app.infrastructure.models import Location
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession


class LocationRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_location(self, location: Location) -> Location:
        """Adds a new location to the database."""
        self.session.add(location)
        await self.session.commit()
        await self.session.refresh(location)
        return location

    async def get_all_locations(self) -> List[Location]:
        """Retrieves all locations from the database."""
        result = await self.session.execute(select(Location))
        return result.scalars().all()

    async def get_location_by_id(self, location_id: int) -> Optional[Location]:
        """Fetches a location by its ID."""
        result = await self.session.execute(
            select(Location).where(Location.id == location_id)
        )
        return result.scalar_one_or_none()
