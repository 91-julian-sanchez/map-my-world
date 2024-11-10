from app.domain.services.location_service import LocationService
from app.infrastructure.models import Location


async def create_location(session, location: Location):
    service = LocationService(session)
    return await service.create_location(location)
