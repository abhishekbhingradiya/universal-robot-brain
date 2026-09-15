from backend.database.session import (
    SessionLocal
)

from backend.models.orm.skill_history_model import (
    SkillHistoryModel
)


class SkillHistoryRepository:

    def create(
        self,
        skill_name,
        version,
        fitness
    ):

        session = SessionLocal()

        try:

            row = SkillHistoryModel(
                skill_name=skill_name,
                version=version,
                fitness=fitness
            )

            session.add(row)

            session.commit()

            return row

        finally:

            session.close()

    def get_skill_history(
        self,
        skill_name
    ):

        session = SessionLocal()

        try:

            return (
                session.query(
                    SkillHistoryModel
                )
                .filter(
                    SkillHistoryModel.skill_name
                    == skill_name
                )
                .order_by(
                    SkillHistoryModel.version
                )
                .all()
            )

        finally:

            session.close()