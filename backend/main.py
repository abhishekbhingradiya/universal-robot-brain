from fastapi import FastAPI
from backend.api.v1.dashboard import (
    router as dashboard_router
)
from backend.api.skills.routes import (
    router as skill_router
)

from backend.api.knowledge.global_routes import (
    router as global_router
)

from backend.api.v1.health import (
    router as health_router
)

from backend.api.v1.skills import (
    router as api_skill_router
)

from backend.api.v1.network import (
    router as network_router
)

from backend.api.v1.robots import (
    router as robot_router
)
from backend.api.v1.experiences import (
    router as experience_router
)
from backend.api.v1.federation import (
    router as federation_router
)
app = FastAPI(
    title="Universal Robot Brain",
    version="0.3"
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

app.include_router(
    health_router,
    prefix="/api/v1",
    tags=["Health"]
)

app.include_router(
    api_skill_router,
    prefix="/api/v1",
    tags=["Skills API"]
)

app.include_router(
    network_router,
    prefix="/api/v1",
    tags=["Network API"]
)

app.include_router(
    robot_router,
    prefix="/api/v1",
    tags=["Robot API"]
)
app.include_router(
    dashboard_router,
    prefix="/api/v1",
    tags=["Dashboard"]
)
app.include_router(
    experience_router,
    prefix="/api/v1",
    tags=["Experience API"]
)
app.include_router(
    federation_router,
    prefix="/api/v1",
    tags=["Federation API"]
)