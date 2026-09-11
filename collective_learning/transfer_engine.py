class TransferEngine:

    def transfer(
            self,
            skill,
            robot):

        robot.learned_skills.append(skill)

        return {
            "robot": robot.robot_id,
            "skill": skill.name,
            "status": "transferred"
        }