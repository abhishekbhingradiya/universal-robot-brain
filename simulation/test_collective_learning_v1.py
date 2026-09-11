from simulation.robots.robot import Robot

robots = []

for i in range(10):
    robots.append(Robot(f"robot-{i}"))

print("Network Created")

for robot in robots:
    print(
        f"{robot.robot_id} | skills: {len(robot.learned_skills)}"
    )