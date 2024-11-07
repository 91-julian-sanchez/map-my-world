from typing import Dict

from fastapi import FastAPI

app = FastAPI()


@app.get("/health")
def read_health() -> Dict[str, str]:
    return {"status": "ok"}
