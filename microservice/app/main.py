from typing import Dict

from app.interfaces.api.categories import router as category_router
from app.interfaces.api.location import router as location_router
from fastapi import FastAPI

app = FastAPI()


@app.get("/health")
def read_health() -> Dict[str, str]:
    return {"status": "Microservice run..."}


app.include_router(location_router)
app.include_router(category_router)
