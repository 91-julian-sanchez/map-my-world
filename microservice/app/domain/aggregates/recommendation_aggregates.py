from typing import List, Optional

from app.infrastructure.repositories.recommendation_repository import \
    RecommendationRepository


class RecommendationAggregate:
    def __init__(self, session):
        self.session = session
        self.repository = RecommendationRepository(session)

    async def get_combinations_category_location(self) -> List[dict]:
        """
        Get all combinations of Location and Category.
        """
        return await self.repository.get_combinations_category_location()

    async def get_combinations_with_review(
        self, days_since_last_review: Optional[int] = None
    ) -> set:
        """
        Get combinations that already exist in RecommendationReview.
        Filters within the last 'days_since_last_review' days.
        If 'days_since_last_review' is None, all combinations are returned.
        """
        return await self.repository.get_combinations_with_review(
            days_since_last_review
        )

    async def get_combinations_without_review(
        self,
        days_since_last_review: Optional[int] = None,
        limit: int = 10,
        offset: int = 0,
    ) -> List[dict]:
        """
        Get combinations have not been reviewed
        in the last 'days_since_last_review' days.
        """
        combinations = await self.get_combinations_category_location()
        existing_combinations = await self.get_combinations_with_review(
            days_since_last_review
        )

        # Filter combinations have not been reviewed
        not_in_review = [
            combination
            for combination in combinations
            if (combination["location_id"], combination["category_id"])
            not in existing_combinations
        ]

        # Apply pagination
        return not_in_review[offset : offset + limit]
