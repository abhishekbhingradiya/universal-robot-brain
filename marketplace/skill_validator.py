class SkillValidator:

    def validate(self, skill):

        if "strategy" not in skill:
            return False

        return True