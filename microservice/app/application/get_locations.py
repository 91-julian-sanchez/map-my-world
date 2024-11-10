from app.domain.services.location_service import LocationService
from sqlmodel.ext.asyncio.session import AsyncSession


async def get_locations(session: AsyncSession):
    service = LocationService(session)
    return await service.get_all_locations()
