class SkillInstaller:

    def install(
            self,
            robot,
            skill):

        robot.learned_skills.append(skill)

        return True