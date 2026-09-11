from simulation.robots.robot import Robot

robots = []

for i in range(100):

    robots.append(
        Robot(
            f"robot-{i}"
        )
    )

print(
    f"Network Size = {len(robots)}"
)