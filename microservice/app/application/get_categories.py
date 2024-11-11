from app.domain.services.category_service import CategoryService


async def get_categories(session):
    service = CategoryService(session)
    return await service.get_all_categories()
