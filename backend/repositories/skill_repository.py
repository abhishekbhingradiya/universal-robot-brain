from backend.database.session import (
    SessionLocal
)

from backend.models.orm.skill_model import (
    SkillModel
)


class SkillRepository:

    def save(
        self,
        strategy,
        avg_reward
    ):

        session = SessionLocal()

        try:

            skill = SkillModel(
                strategy=strategy,
                avg_reward=avg_reward
            )

            session.add(
                skill
            )

            session.commit()

            return skill

        finally:

            session.close()

    def get_all(self):

        session = SessionLocal()

        try:

            return session.query(
                SkillModel
            ).all()

        finally:

            session.close()