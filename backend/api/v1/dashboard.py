from fastapi import APIRouter

from backend.services.network_memory import (
    get_global_skills
)

from backend.services.robot_service import (
    RobotService
)


router = APIRouter()

robot_service = RobotService()


@router.get("/dashboard/overview")
def dashboard_overview():

    skills = get_global_skills()

    return {
        "total_skills": len(skills),
        "total_robots": robot_service.get_robot_count(),
        "network_status": "active"
    }


@router.get("/dashboard/skills")
def dashboard_skills():

    skills = get_global_skills()

    return {
        "skills": skills
    }