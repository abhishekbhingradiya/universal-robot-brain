from fastapi import APIRouter

from backend.services.network_memory import (
    get_global_skills
)

router = APIRouter()


@router.get("/dashboard/overview")
def dashboard_overview():

    skills = get_global_skills()

    return {
        "total_skills": len(skills),
        "network_status": "active"
    }


@router.get("/dashboard/skills")
def dashboard_skills():

    skills = get_global_skills()

    return {
        "skills": skills
    }
