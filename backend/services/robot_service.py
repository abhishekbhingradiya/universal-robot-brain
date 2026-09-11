from backend.repositories.robot_repository import (
    RobotRepository
)


class RobotService:

    def __init__(self):

        self.repo = RobotRepository()

    def register_robot(
        self,
        robot_id,
        robot_type="general"
    ):

        return self.repo.create(
            robot_id,
            robot_type
        )

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