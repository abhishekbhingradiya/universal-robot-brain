from simulation.robots.robot import Robot

robot = Robot("R1")

robot.upgrade_skill(
    "maze_navigation",
    1
)

print(
    robot.get_active_version(
        "maze_navigation"
    )
)

robot.upgrade_skill(
    "maze_navigation",
    2
)

print(
    robot.get_active_version(
        "maze_navigation"
    )
)

print()

print(
    robot.get_status()
)