from backend.repositories.activity_repository import (
    ActivityRepository
)


class ActivityService:

    def __init__(self):

        self.repo = ActivityRepository()

    def create_activity(
        self,
        event_type,
        entity
    ):

        return self.repo.create(
            event_type,
            entity
        )

    def get_activities(
        self
    ):

        return self.repo.get_all()

    def log_robot_registered(
        self,
        robot_id
    ):

        return self.create_activity(
            "robot_registered",
            robot_id
        )

    def log_experience_created(
        self,
        robot_id
    ):

        return self.create_activity(
            "experience_created",
            robot_id
        )

    def log_federation_created(
        self,
        node_id
    ):

        return self.create_activity(
            "federation_node_created",
            node_id
        )