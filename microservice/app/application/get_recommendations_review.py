from app.domain.services.review_service import RecommendationReviewService


async def get_recommendations_review(session):
    service = RecommendationReviewService(session)
    return await service.get_all_recommendation_reviews()
