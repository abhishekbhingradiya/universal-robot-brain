from fastapi import APIRouter

from pydantic import BaseModel

from backend.services.skill_evolution_service import (
    SkillEvolutionService
)

router = APIRouter()

service = (
    SkillEvolutionService()
)


class EvolutionRequest(
    BaseModel
):

    skill_name: str

    fitness: float


@router.post(
    "/skills/evolve"
)
def evolve_skill(
    request: EvolutionRequest
):

    return (
        service.evolve_skill(
            request.skill_name,
            request.fitness
        )
    )