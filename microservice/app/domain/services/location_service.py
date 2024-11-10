from typing import List

from app.infrastructure.models import Location
from app.infrastructure.repositories.location_repository import \
    LocationRepository
from sqlmodel.ext.asyncio.session import AsyncSession


class LocationService:
    def __init__(self, session: AsyncSession):
        self.repository = LocationRepository(session)

    async def create_location(self, location: Location) -> Location:
        """Creates a new location using the repository."""
        return await self.repository.create_location(location)

    async def get_all_locations(self) -> List[Location]:
        """Retrieves all locations using the repository."""
        return await self.repository.get_all_locations()
