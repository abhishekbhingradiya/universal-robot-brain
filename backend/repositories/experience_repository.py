from backend.database.session import (
    SessionLocal
)

from backend.models.orm.experience_model import (
    ExperienceModel
)

from backend.logger import logger


class ExperienceRepository:

    def create(
        self,
        robot_id,
        task,
        strategy,
        reward
    ):

        session = SessionLocal()

        try:

            experience = ExperienceModel(
                robot_id=robot_id,
                task=task,
                strategy=strategy,
                reward=reward
            )

            session.add(
                experience
            )

            session.commit()

            logger.info(
                f"Experience stored: "
                f"{robot_id}"
            )

            return experience

        finally:

            session.close()

    def get_all(self):

        session = SessionLocal()

        try:

            return (
                session.query(
                    ExperienceModel
                )
                .all()
            )

        finally:

            session.close()

    def get_by_robot_id(
        self,
        robot_id
    ):

        session = SessionLocal()

        try:

            return (
                session.query(
                    ExperienceModel
                )
                .filter(
                    ExperienceModel.robot_id
                    == robot_id
                )
                .all()
            )

        finally:

            session.close()

    def count(self):

        session = SessionLocal()

        try:

            return (
                session.query(
                    ExperienceModel
                )
                .count()
            )

        finally:

            session.close()