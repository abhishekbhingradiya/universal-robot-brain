from fastapi import APIRouter

from backend.services.network_memory import (
    get_global_skills
)

from backend.services.robot_service import (
    RobotService
)

from backend.services.experience_service import (
    ExperienceService
)


router = APIRouter()

robot_service = RobotService()

experience_service = (
    ExperienceService()
)


@router.get(
    "/dashboard/overview"
)
def dashboard_overview():

    skills = get_global_skills()

    return {
        "total_skills":
            len(skills),

        "total_robots":
            robot_service.get_robot_count(),

        "total_experiences":
            experience_service.get_experience_count(),

        "network_status":
            "active"
    }


@router.get(
    "/dashboard/skills"
)
def dashboard_skills():

    skills = get_global_skills()

    return {
        "skills": skills
    }