class SkillRegistry:

    def __init__(self):

        self.skills = {}

    def register(
        self,
        skill_name,
        version,
        fitness
    ):

        self.skills[skill_name] = {
            "version": version,
            "fitness": fitness
        }

    def get(
        self,
        skill_name
    ):

        return self.skills.get(
            skill_name
        )

    def all(self):

        return self.skills