from simulation.robots.robot import Robot


class Fleet:

    def __init__(
        self,
        size
    ):

        self.robots = [
            Robot(
                f"robot-{i}"
            )
            for i in range(size)
        ]

    def get_robots(self):

        return self.robots