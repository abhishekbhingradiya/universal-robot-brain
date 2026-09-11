from simulation.robots.robot import Robot

robot = Robot(
    "robot-001"
)

robot.generate_experience()

robot.inherit_network_memory()

print()
print("Logging demo complete")