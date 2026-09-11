import random


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