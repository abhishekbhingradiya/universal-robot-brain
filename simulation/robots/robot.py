import random

from backend.services.network_memory import (
    get_global_skills
)


class Robot:

    def __init__(self, robot_id):

        self.robot_id = robot_id

        self.learned_skills = []

        self.active_skill_versions = {}

        self.experience_count = 0

    def generate_experience(self):

        strategies = {
            "left_wall": random.uniform(0.65, 0.75),
            "right_wall": random.uniform(0.50, 0.65),
            "random_walk": random.uniform(0.30, 0.55)
        }

        strategy = random.choice(
            list(strategies.keys())
        )

        reward = strategies[strategy]

        self.experience_count += 1

        return {
            "robot_id": self.robot_id,
            "task": "maze_navigation",
            "strategy": strategy,
            "reward": reward,
            "success": random.random() < reward
        }

    def learn_skill(self, skill):

        self.learned_skills.append(
            skill
        )

    def install_skill(self, skill):

        self.learned_skills.append(
            skill
        )

        skill_name = skill.get(
            "name",
            "unknown_skill"
        )

        skill_version = skill.get(
            "version",
            1
        )

        self.active_skill_versions[
            skill_name
        ] = skill_version

    def inherit_network_memory(self):

        skills = get_global_skills()

        for skill in skills:

            self.learned_skills.append(
                skill
            )

    def increment_experience(self):

        self.experience_count += 1

    def upgrade_skill(
        self,
        skill_name,
        version
    ):

        self.active_skill_versions[
            skill_name
        ] = version

    def get_active_version(
        self,
        skill_name
    ):

        return self.active_skill_versions.get(
            skill_name
        )

    def get_skill_count(self):

        return len(
            self.learned_skills
        )

    def get_status(self):

        return {
            "robot_id": self.robot_id,
            "experience_count":
                self.experience_count,
            "skill_count":
                len(self.learned_skills),
            "active_skill_versions":
                self.active_skill_versions
        }