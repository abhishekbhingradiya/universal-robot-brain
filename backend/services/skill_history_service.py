from backend.repositories.skill_history_repository import (
    SkillHistoryRepository
)


class SkillHistoryService:

    def __init__(self):

        self.repo = (
            SkillHistoryRepository()
        )

    def record_version(
        self,
        skill_name,
        version,
        fitness
    ):

        return self.repo.create(
            skill_name,
            version,
            fitness
        )

    def get_timeline(
        self,
        skill_name
    ):

        return self.repo.get_skill_history(
            skill_name
        )