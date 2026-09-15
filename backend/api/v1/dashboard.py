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

from backend.services.federation_service import (
    FederationService
)


router = APIRouter()

robot_service = RobotService()

experience_service = (
    ExperienceService()
)

federation_service = (
    FederationService()
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

        "federation_nodes":
            federation_service.get_node_count(),

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