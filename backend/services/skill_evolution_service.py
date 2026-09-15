from backend.services.skill_history_service import (
    SkillHistoryService
)

from backend.services.activity_service import (
    ActivityService
)


class SkillEvolutionService:

    def __init__(self):

        self.history_service = (
            SkillHistoryService()
        )

        self.activity_service = (
            ActivityService()
        )

    def evolve_skill(
        self,
        skill_name,
        fitness
    ):

        timeline = (
            self.history_service
            .get_timeline(
                skill_name
            )
        )

        if not timeline:

            version = 1

        else:

            latest = timeline[-1]

            if fitness <= latest.fitness:

                return {
                    "evolved": False,
                    "reason":
                        "fitness_not_improved"
                }

            version = (
                latest.version + 1
            )

        self.history_service.record_version(
            skill_name,
            version,
            fitness
        )

        self.activity_service.create_activity(
            "skill_evolved",
            skill_name
        )

        return {
            "evolved": True,
            "skill_name":
                skill_name,
            "version":
                version,
            "fitness":
                fitness
        }
