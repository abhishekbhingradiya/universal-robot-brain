from backend.logger import logger


class SkillInstaller:

    def install(
        self,
        robot,
        skill
    ):

        robot.install_skill(
            skill
        )

        logger.info(
            f"Installed skill "
            f"{skill.get('name', 'unknown')} "
            f"on {robot.robot_id}"
        )

        return True