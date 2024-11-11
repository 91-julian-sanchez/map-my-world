from typing import List

from app.infrastructure.models import Category
from app.infrastructure.repositories.category_repository import \
    CategoryRepository


class CategoryService:
    def __init__(self, session):
        self.repository = CategoryRepository(session)

    async def create_Category(self, Category: Category) -> Category:
        """Creates a new category using the repository."""
        return await self.repository.create_category(Category)

    async def get_all_categories(self) -> List[Category]:
        """Retrieves all Categorys using the repository."""
        return await self.repository.get_all_categories()
