from app.domain.services.location_service import LocationService


async def get_locations(session):
    service = LocationService(session)
    return await service.get_all_locations()
