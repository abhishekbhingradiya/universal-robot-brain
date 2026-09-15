from backend.services.skill_evolution_service import (
    SkillEvolutionService
)

service = (
    SkillEvolutionService()
)

print(
    service.evolve_skill(
        "left_wall",
        0.95
    )
)