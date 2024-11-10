from app.domain.services.location_service import LocationService
from app.infrastructure.models import Category


async def create_location(session, category: Category):
    service = LocationService(session)
    return await service.create_location(category)
