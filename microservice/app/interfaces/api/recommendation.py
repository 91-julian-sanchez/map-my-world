from datetime import datetime
from typing import List, Optional

from app.application.create_review import create_recommendation_review
from app.application.get_combinations_without_review import \
    get_combinations_without_review
from app.application.get_recommendations_review import \
    get_recommendations_review
from app.core.config import settings
from app.domain.schemas.recommendation import (RecommendationReviewCreate,
                                               RecommendationReviewResponse)
from app.infrastructure.db import get_session
from app.infrastructure.models import RecommendationReview
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel.ext.asyncio.session import AsyncSession

router = APIRouter()


@router.get(
    "/recommendations/review", response_model=List[RecommendationReviewResponse]
)
async def get_recommendations_review_endpoint(
    session: AsyncSession = Depends(get_session),
):
    try:
        return await get_recommendations_review(session)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/recommendations/review")
async def add_recommendation_review(
    recommendation_review: RecommendationReviewCreate,
    session: AsyncSession = Depends(get_session),
):
    try:
        recommendation_review = RecommendationReview(
            location_id=recommendation_review.location_id,
            category_id=recommendation_review.category_id,
            reviewed_at=datetime.utcnow(),
        )
        recommendation_review_created = await create_recommendation_review(
            session, recommendation_review
        )
        return recommendation_review_created
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/recommendations/not-reviewed", response_model=List[dict])
async def get_combinations_without_review_endpoint(
    session: AsyncSession = Depends(get_session),
    days_since_last_review: Optional[int] = settings.days_since_last_review,
    limit: int = 10,
    offset: int = 0,
):
    try:
        not_in_review = await get_combinations_without_review(
            session, days_since_last_review, limit, offset
        )
        return not_in_review

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
