class SkillMarketplace:

    def __init__(self):

        self.skills = []

    def publish(self, skill):

        self.skills.append(skill)

    def list_skills(self):

        return self.skills