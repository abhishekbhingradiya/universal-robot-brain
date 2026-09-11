class FleetUpgrade:

    def upgrade_fleet(
        self,
        robots,
        skill
    ):

        for robot in robots:

            robot.install_skill(
                skill
            )

        return len(
            robots
        )