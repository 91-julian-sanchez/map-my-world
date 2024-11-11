from app.domain.aggregates.recommendation_aggregates import \
    RecommendationAggregate


async def get_combinations_without_review(
    session, days_since_last_review: int, limit: int, offset: int
):
    service = RecommendationAggregate(session)
    return await service.get_combinations_without_review(
        days_since_last_review, limit, offset
    )
