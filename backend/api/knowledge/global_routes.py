from fastapi import APIRouter
from backend.services.network_memory \
    import get_global_skills

router = APIRouter()


@router.get("/global")

def global_skills():

    return get_global_skills()