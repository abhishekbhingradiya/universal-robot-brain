from backend.repositories.skill_repository import (
    SkillRepository
)


def test_repository_save():

    repo = SkillRepository()

    skill = repo.save(
        "test_strategy",
        0.88
    )

    assert (
        skill.strategy
        ==
        "test_strategy"
    )