from typing import List, Optional

from app.infrastructure.models import Category
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession


class CategoryRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_category(self, category: Category) -> Category:
        """Adds a new category to the database."""
        self.session.add(category)
        await self.session.commit()
        await self.session.refresh(category)
        return category

    async def get_all_categories(self) -> List[Category]:
        """Retrieves all categories from the database."""
        result = await self.session.execute(select(Category))
        return result.scalars().all()

    async def get_category_by_id(self, category_id: int) -> Optional[Category]:
        """Fetches a category by its ID."""
        result = await self.session.execute(
            select(Category).where(Category.id == category_id)
        )
        return result.scalar_one_or_none()
