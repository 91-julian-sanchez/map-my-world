from typing import Dict

from app.interfaces.api.categories import router as category_router
from app.interfaces.api.location import router as location_router
from app.interfaces.api.recommendation import router as recommendation_router
from fastapi import FastAPI

app = FastAPI(
    title="Map My World API",
    description="This is a microservice API that manages categories, locations, and recommendations.",  # noqa  E501
    version="1.0.0",
)


@app.get(
    "/health",
    response_model=Dict[str, str],
    summary="Health Check",
    description="Endpoint to check the health of the microservice.",
)
def read_health() -> Dict[str, str]:
    """
    Health check endpoint to verify if the microservice is up and running.
    It responds with a status and a message.
    """
    return {"status": "ok", "message": "Microservice is running..."}


# Including the routers for different modules (location, category, recommendation)
app.include_router(location_router)
app.include_router(category_router)
app.include_router(recommendation_router)
