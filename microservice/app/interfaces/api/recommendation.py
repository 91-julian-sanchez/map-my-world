from datetime import datetime
from typing import List, Optional

from app.application.create_review import create_recommendation_review
from app.application.get_combinations_without_review import \
    get_combinations_without_review
from app.application.get_recommendations_review import \
    get_recommendations_review
from app.core.config import settings
from app.domain.schemas.recommendation import (
    RecommendationReviewCreate, RecommendationReviewResponse,
    RecommendationsNotReviewedResponse)
from app.infrastructure.db import get_session
from app.infrastructure.models import RecommendationReview
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel.ext.asyncio.session import AsyncSession

router = APIRouter()


@router.get(
    "/recommendations/review",
    response_model=List[RecommendationReviewResponse],
    summary="Retrieve Reviews of Recommendations",
    description="Get a list of all reviews for recommendations.",
    tags=["Recommendations review"],
)
async def get_recommendations_review_endpoint(
    session: AsyncSession = Depends(get_session),
):
    """
    Endpoint to retrieve all recommendation reviews from the database.
    - **session**: Database session dependency for accessing the database.
    """
    try:
        return await get_recommendations_review(session)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post(
    "/recommendations/review",
    response_model=RecommendationReview,
    summary="Add a Review for a Recommendation",
    description="Create a review for a recommendation.",
    tags=["Recommendations review"],
)
async def add_recommendation_review_endpoint(
    recommendation_review: RecommendationReviewCreate,
    session: AsyncSession = Depends(get_session),
):
    """
    Endpoint to add a review for a recommendation.
    - **recommendation_review**: Data for the new review.
    - **session**: Database session dependency for accessing the database.
    """
    try:
        recommendation_review = RecommendationReview(
            location_id=recommendation_review.location_id,
            category_id=recommendation_review.category_id,
            reviewed_at=datetime.utcnow(),
        )
        return await create_recommendation_review(session, recommendation_review)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get(
    "/recommendations/not-reviewed",
    response_model=List[RecommendationsNotReviewedResponse],
    summary="Get Recommendations Without Reviews",
    description="Get a list of recommendation that have not yet been reviewed.",
    tags=["Recommendations review"],
)
async def get_combinations_without_review_endpoint(
    session: AsyncSession = Depends(get_session),
    days_since_last_review: Optional[int] = settings.days_since_last_review,
    limit: int = 10,
    offset: int = 0,
):
    """
    Endpoint to retrieve locations and categories that have not yet been reviewed.
    - **session**: Database session dependency for accessing the database.
    - **days_since_last_review**: filter by have not been reviewed since the given days.
    - **limit**: Number of results to return.
    - **offset**: The offset for pagination of results.
    """
    try:
        not_in_review = await get_combinations_without_review(
            session, days_since_last_review, limit, offset
        )
        return not_in_review

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
