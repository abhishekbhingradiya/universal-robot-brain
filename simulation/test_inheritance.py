from simulation.robots.robot import Robot

robot = Robot("new_robot")

robot.inherit_network_memory()

print(robot.learned_skills)