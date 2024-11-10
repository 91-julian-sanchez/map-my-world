from typing import List

from app.infrastructure.models import RecommendationReview
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession


class RecommendationReviewRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_recommendation_review(
        self, review: RecommendationReview
    ) -> RecommendationReview:
        """Adds a new recommendation review to the database."""
        self.session.add(review)
        await self.session.commit()
        await self.session.refresh(review)
        return review

    async def get_all_recommendation_reviews(self) -> List[RecommendationReview]:
        """Retrieves all recommendation reviews from the database."""
        result = await self.session.execute(select(RecommendationReview))
        return result.scalars().all()
