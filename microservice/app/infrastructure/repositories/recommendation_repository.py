from datetime import datetime, timedelta
from typing import List, Optional, Set, Tuple

from app.infrastructure.models import Category, Location, RecommendationReview
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select


class RecommendationRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_combinations(self) -> List[dict]:
        """
        Get all combinations of Location and Category.
        """
        stmt = select(Location, Category)
        results = await self.session.execute(stmt)
        combinations = [
            {"location_id": loc.id, "category_id": cat.id} for loc, cat in results
        ]

        return combinations

    async def get_combinations_category_location(self) -> List[dict]:
        """
        Get all combinations of Location and Category.
        """
        stmt = select(Location, Category)
        results = await self.session.execute(stmt)
        combinations = [
            {
                "location": {
                    "id": loc.id,
                    "name": loc.name,
                },
                "category": {
                    "id": cat.id,
                    "name": cat.name,
                },
            }
            for loc, cat in results
        ]

        return combinations

    async def get_combinations_with_review(
        self, days_since_last_review: Optional[int] = None
    ) -> Set[Tuple[int, int]]:
        """
        Get combinations reviewed.
        Filters within the last 'days_since_last_review' days.
        If 'days_since_last_review' is None, all combinations are returned.
        """
        since_date = (
            datetime.utcnow() - timedelta(days=days_since_last_review)
            if days_since_last_review
            else None
        )

        # Select distinct combinations from the RecommendationReview table
        existing_combinations_stmt = select(
            RecommendationReview.location_id,
            RecommendationReview.category_id,
            RecommendationReview.reviewed_at,
        ).distinct()
        existing_results = await self.session.execute(existing_combinations_stmt)

        # Build the set of combinations
        if since_date:
            existing_combinations = {
                (rec_loc_id, rec_cat_id): reviewed_at
                for rec_loc_id, rec_cat_id, reviewed_at in existing_results
                if reviewed_at >= since_date
            }
        else:
            existing_combinations = {
                (rec_loc_id, rec_cat_id): reviewed_at
                for rec_loc_id, rec_cat_id, reviewed_at in existing_results
            }

        return existing_combinations
