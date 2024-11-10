from datetime import datetime

from app.application.create_review import create_recommendation_review
from app.domain.schemas.recommendation import RecommendationReviewCreate
from app.infrastructure.db import get_session
from app.infrastructure.models import RecommendationReview
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel.ext.asyncio.session import AsyncSession

router = APIRouter()


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
        return {"status": "success", "review": recommendation_review_created}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
