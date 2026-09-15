from backend.database.session import (
    SessionLocal
)

from backend.models.orm.activity_model import (
    ActivityModel
)


class ActivityRepository:

    def create(
        self,
        event_type,
        entity
    ):

        session = SessionLocal()

        try:

            activity = ActivityModel(
                event_type=event_type,
                entity=entity
            )

            session.add(activity)

            session.commit()

            return activity

        finally:

            session.close()

    def get_all(self):

        session = SessionLocal()

        try:

            return (
                session.query(
                    ActivityModel
                )
                .order_by(
                    ActivityModel.id.desc()
                )
                .all()
            )

        finally:

            session.close()