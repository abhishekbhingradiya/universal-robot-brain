from backend.database.session import (
    SessionLocal
)

from backend.models.orm.skill_model import (
    SkillModel
)

from backend.logger import logger


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

            logger.info(
                f"Saved skill: {strategy}"
            )

            return skill

        finally:

            session.close()

    def get_all(self):

        session = SessionLocal()

        try:

            skills = session.query(
                SkillModel
            ).all()

            logger.info(
                f"Loaded {len(skills)} skills"
            )

            return skills

        finally:

            session.close()