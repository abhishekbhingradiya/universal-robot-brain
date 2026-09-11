from fastapi import APIRouter

from backend.repositories.skill_repository import (
    SkillRepository
)

router = APIRouter()

repo = SkillRepository()


@router.get("/skills")
def get_skills():

    skills = repo.get_all()

    return [
        {
            "id": skill.id,
            "strategy": skill.strategy,
            "avg_reward": skill.avg_reward
        }
        for skill in skills
    ]