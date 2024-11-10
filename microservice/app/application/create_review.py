from app.domain.services.review_service import RecommendationReviewService
from app.infrastructure.models import RecommendationReview
from sqlmodel.ext.asyncio.session import AsyncSession


async def create_recommendation_review(
    session: AsyncSession, review: RecommendationReview
):
    service = RecommendationReviewService(session)
    return await service.create_recommendation_review(review)
