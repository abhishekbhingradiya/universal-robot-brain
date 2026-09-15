from backend.repositories.experience_repository import (
    ExperienceRepository
)


class ExperienceService:

    def __init__(self):

        self.repo = (
            ExperienceRepository()
        )

    def create_experience(
        self,
        robot_id,
        task,
        strategy,
        reward
    ):

        return self.repo.create(
            robot_id,
            task,
            strategy,
            reward
        )

    def get_experiences(self):

        return self.repo.get_all()

    def get_robot_experiences(
        self,
        robot_id
    ):

        return self.repo.get_by_robot_id(
            robot_id
        )

    def get_experience_count(
        self
    ):

        return self.repo.count()