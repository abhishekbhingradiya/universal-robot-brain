from backend.repositories.skill_repository import (
    SkillRepository
)


repo = SkillRepository()


def save_global_skill(skill):

    repo.save(
        strategy=skill["strategy"],
        avg_reward=skill["avg_reward"]
    )


def get_global_skills():

    skills = repo.get_all()

    return [
        (
            skill.strategy,
            skill.avg_reward
        )
        for skill in skills
    ]