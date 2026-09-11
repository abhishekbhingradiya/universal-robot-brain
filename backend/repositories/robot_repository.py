from backend.database.session import (
    SessionLocal
)

from backend.models.orm.robot_model import (
    RobotModel
)

from backend.logger import logger


class RobotRepository:

    def create(
        self,
        robot_id,
        robot_type="general"
    ):

        session = SessionLocal()

        try:

            existing_robot = (
                session.query(
                    RobotModel
                )
                .filter(
                    RobotModel.robot_id
                    == robot_id
                )
                .first()
            )

            if existing_robot:

                logger.info(
                    f"Robot already exists: "
                    f"{robot_id}"
                )

                return existing_robot

            robot = RobotModel(
                robot_id=robot_id,
                robot_type=robot_type,
                status="active"
            )

            session.add(
                robot
            )

            session.commit()

            logger.info(
                f"Robot registered: "
                f"{robot_id}"
            )

            return robot

        finally:

            session.close()

    def get_all(self):

        session = SessionLocal()

        try:

            return (
                session.query(
                    RobotModel
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
                    RobotModel
                )
                .filter(
                    RobotModel.robot_id
                    == robot_id
                )
                .first()
            )

        finally:

            session.close()

    def count(self):

        session = SessionLocal()

        try:

            return (
                session.query(
                    RobotModel
                )
                .count()
            )

        finally:

            session.close()