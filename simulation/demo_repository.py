from backend.repositories.skill_repository import (
    SkillRepository
)

repo = SkillRepository()

repo.save(
    "left_wall",
    0.71
)

skills = repo.get_all()

print()

for skill in skills:

    print(
        skill.id,
        skill.strategy,
        skill.avg_reward
    )