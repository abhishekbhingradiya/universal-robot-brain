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