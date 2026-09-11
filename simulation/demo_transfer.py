from robots.robot import Robot

robot_a = Robot("R001")

experiences = []

for _ in range(100):
    experiences.append(
        robot_a.generate_experience()
    )

print("Experience count:", len(experiences))