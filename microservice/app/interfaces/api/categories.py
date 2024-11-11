from typing import List

from app.application.create_category import create_category
from app.application.get_categories import get_categories
from app.domain.schemas.category import CategoryCreate
from app.domain.schemas.recommendation import CategoryResponse
from app.infrastructure.db import get_session
from app.infrastructure.models import Category
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel.ext.asyncio.session import AsyncSession

router = APIRouter()


@router.get(
    "/categories",
    response_model=List[CategoryResponse],
    summary="Retrieve Categories",
    description="Get a list of all categories available.",
    tags=["Categories"],
)
async def get_categories_endpoint(session: AsyncSession = Depends(get_session)):
    """
    Endpoint to retrieve all categories from the database.
    - **session**: Database session dependency for database access.
    """
    try:
        return await get_categories(session)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post(
    "/categories",
    response_model=CategoryResponse,
    summary="Add a New Category",
    description="Create and add a new category.",
    tags=["Categories"],
)
async def add_category(
    category: CategoryCreate, session: AsyncSession = Depends(get_session)
):
    """
    Endpoint to add a new category to the database.
    - **category**: Category data to be added.
    - **session**: Database session dependency for database access.
    """
    try:
        category_model = Category(name=category.name)
        return await create_category(session, category_model)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
