from simulation.robots.robot import Robot

robots = []

for i in range(10):

    robots.append(
        Robot(
            f"robot-{i}"
        )
    )

print(
    f"Created {len(robots)} robots"
)