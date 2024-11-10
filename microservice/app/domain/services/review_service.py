from typing import List

from app.infrastructure.models import RecommendationReview
from app.infrastructure.repositories.review_repository import \
    RecommendationReviewRepository
from sqlmodel.ext.asyncio.session import AsyncSession


class RecommendationReviewService:
    def __init__(self, session: AsyncSession):
        self.repository = RecommendationReviewRepository(session)

    async def create_recommendation_review(
        self, location: RecommendationReview
    ) -> RecommendationReview:
        """Creates a new recommendation review using the repository."""
        return await self.repository.create_recommendation_review(location)

    async def get_all_recommendation_reviews(self) -> List[RecommendationReview]:
        """Retrieves all recommendation reviews using the repository."""
        return await self.repository.get_all_recommendation_reviews()
