from app.application.create_category import create_category
from app.application.get_categories import get_categories
from app.domain.schemas.category import CategoryCreate
from app.infrastructure.db import get_session
from app.infrastructure.models import Category
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel.ext.asyncio.session import AsyncSession

router = APIRouter()


@router.get("/categories")
async def get_categories_endpoint(session: AsyncSession = Depends(get_session)):
    try:
        return {"status": "ok", "categories": await get_categories(session)}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/categories")
async def add_category(
    category: CategoryCreate, session: AsyncSession = Depends(get_session)
):
    try:
        category_model = Category(name=category.name)
        category_created = await create_category(session, category_model)
        return {"status": "ok", "category": category_created}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
