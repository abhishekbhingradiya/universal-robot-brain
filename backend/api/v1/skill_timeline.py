from fastapi import APIRouter

from backend.services.skill_history_service import (
    SkillHistoryService
)

router = APIRouter()

service = SkillHistoryService()


@router.get(
    "/skills/{skill_name}/timeline"
)
def get_timeline(
    skill_name: str
):

    timeline = (
        service.get_timeline(
            skill_name
        )
    )

    return {
        "skill_name": skill_name,
        "versions": [
            {
                "version": item.version,
                "fitness": item.fitness
            }
            for item in timeline
        ]
    }