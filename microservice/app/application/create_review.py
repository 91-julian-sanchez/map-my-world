from app.domain.services.review_service import RecommendationReviewService
from app.infrastructure.models import RecommendationReview


async def create_recommendation_review(session, review: RecommendationReview):
    service = RecommendationReviewService(session)
    return await service.create_recommendation_review(review)
