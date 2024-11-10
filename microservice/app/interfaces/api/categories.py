from app.application.create_location import create_location
from app.domain.schemas.category import CategoryCreate
from app.infrastructure.db import get_session
from app.infrastructure.models import Category
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel.ext.asyncio.session import AsyncSession

router = APIRouter()


@router.post("/categories")
async def add_category(
    category: CategoryCreate, session: AsyncSession = Depends(get_session)
):
    try:
        category_model = Category(name=category.name)
        category_created = await create_location(session, category_model)
        return {"status": "success", "category": category_created}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
