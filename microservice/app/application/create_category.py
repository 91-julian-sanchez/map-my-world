from app.domain.services.location_service import LocationService
from app.infrastructure.models import Category
from sqlmodel.ext.asyncio.session import AsyncSession


async def create_location(session: AsyncSession, category: Category):
    service = LocationService(session)
    return await service.create_location(category)
