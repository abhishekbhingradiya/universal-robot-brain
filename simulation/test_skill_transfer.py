from robots.robot import Robot

robot_a = Robot("A")
robot_b = Robot("B")

skill = {
    "skill": "maze_navigation"
}

robot_b.learned_skills.append(skill)

print(robot_b.learned_skills)