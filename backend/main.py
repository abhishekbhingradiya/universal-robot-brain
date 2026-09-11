from fastapi import FastAPI

from backend.api.skills.routes import router as skill_router
from backend.api.knowledge.global_routes import router as global_router


app = FastAPI(
    title="Universal Robot Brain",
    version="0.1"
)


@app.get("/")
def root():
    return {
        "project": "Universal Robot Brain",
        "status": "online"
    }


app.include_router(
    skill_router,
    prefix="/skills",
    tags=["Skills"]
)

app.include_router(
    global_router,
    prefix="/knowledge",
    tags=["Global Knowledge"]
)