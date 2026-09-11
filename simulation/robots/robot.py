import random


class Robot:

    def __init__(self, robot_id):

        self.robot_id = robot_id

    def generate_experience(self):

        strategies = [
            "left_wall",
            "right_wall",
            "random_walk"
        ]

        strategy = random.choice(strategies)

        return {
            "machine_id": self.robot_id,
            "task": "maze_navigation",
            "strategy": strategy,
            "success": random.random() > 0.3,
            "reward": random.random()
        }