from fastapi import APIRouter

from backend.services.network_memory import (
    get_global_skills
)

router = APIRouter()


@router.get("/network/memory")
def network_memory():

    skills = get_global_skills()

    return {
        "count": len(skills),
        "skills": skills
    }


@router.get("/network/stats")
def network_stats():

    skills = get_global_skills()

    return {
        "total_skills": len(skills)
    }