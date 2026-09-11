from fastapi import APIRouter

router = APIRouter()

robots = []


@router.get("/robots")
def get_robots():

    return {
        "count": len(robots),
        "robots": robots
    }