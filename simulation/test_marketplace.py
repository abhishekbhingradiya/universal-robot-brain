from simulation.robots.robot import Robot

from marketplace.skill_marketplace \
    import SkillMarketplace

from marketplace.skill_installer \
    import SkillInstaller

market = SkillMarketplace()

robot_a = Robot("A")
robot_b = Robot("B")

skill = {
    "strategy": "left_wall",
    "reward": 0.7
}

market.publish(skill)

installer = SkillInstaller()

installer.install(
    robot_b,
    skill
)

print()

print("Marketplace Skills:")

print(
    market.list_skills()
)

print()

print("Robot B Skills:")

print(
    robot_b.learned_skills
)
