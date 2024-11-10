from app.domain.aggregates.recommendation_aggregates import \
    RecommendationAggregate
from app.infrastructure.models import Category


async def get_combinations_without_review(session, category: Category):
    service = RecommendationAggregate(session)
    return await service.get_combinations_without_review(category)
