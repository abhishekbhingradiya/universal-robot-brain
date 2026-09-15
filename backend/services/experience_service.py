from backend.repositories.experience_repository import (
    ExperienceRepository
)

from backend.services.activity_service import (
    ActivityService
)


class ExperienceService:

    def __init__(self):

        self.repo = (
            ExperienceRepository()
        )

        self.activity_service = (
            ActivityService()
        )

    def create_experience(
        self,
        robot_id,
        task,
        strategy,
        reward
    ):

        experience = (
            self.repo.create(
                robot_id,
                task,
                strategy,
                reward
            )
        )

        self.activity_service.log_experience_created(
            robot_id
        )

        return experience

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