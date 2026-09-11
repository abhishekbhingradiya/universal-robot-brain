from backend.logger import logger


class SkillMarketplace:

    def __init__(self):

        self.skills = []

    def publish(
        self,
        skill
    ):

        self.skills.append(
            skill
        )

        logger.info(
            f"Published skill: {skill}"
        )

    def list_skills(
        self
    ):

        logger.info(
            f"Listing {len(self.skills)} skills"
        )

        return self.skills