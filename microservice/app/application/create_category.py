from app.domain.services.category_service import CategoryService
from app.infrastructure.models import Category


async def create_category(session, category: Category):
    service = CategoryService(session)
    return await service.create_Category(category)
