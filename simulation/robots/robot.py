import random
from backend.models import skill
from backend.services.network_memory \
    import get_global_skills

class Robot:

    def __init__(self, robot_id):

        self.robot_id = robot_id
        self.learned_skills = []

    def generate_experience(self):

        strategies = {
            "left_wall": 0.70,
            "right_wall": 0.55,
            "random_walk": 0.40
        }

        strategy = random.choice(
            list(strategies.keys())
        )

        return {
            "robot_id": self.robot_id,
            "task": "maze_navigation",
            "strategy": strategy,
            "reward": strategies[strategy],
            "success": random.random()
            < strategies[strategy]
        }

    def learn_skill(self, skill):

        self.learned_skills.append(skill)

    def inherit_network_memory(self):

     skills = get_global_skills()

     for skill in skills:

        self.learned_skills.append(skill)

    def install_skill(
        self,
        skill):

        self.learned_skills.append(
        skill
    )
        self.experience_count = 0
    def increment_experience(self):

        self.experience_count += 1
