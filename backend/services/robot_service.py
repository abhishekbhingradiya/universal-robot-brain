from backend.repositories.robot_repository import (
    RobotRepository
)

from backend.services.activity_service import (
    ActivityService
)


class RobotService:

    def __init__(self):

        self.repo = RobotRepository()

        self.activity_service = (
            ActivityService()
        )

    def register_robot(
        self,
        robot_id,
        robot_type="general"
    ):

        robot = self.repo.create(
            robot_id,
            robot_type
        )

        self.activity_service.log_robot_registered(
            robot_id
        )

        return robot

    def get_robots(
        self
    ):

        return self.repo.get_all()

    def get_robot(
        self,
        robot_id
    ):

        return self.repo.get_by_robot_id(
            robot_id
        )

    def get_robot_count(
        self
    ):

        return self.repo.count()