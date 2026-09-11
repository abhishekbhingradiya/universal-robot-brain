from simulation.robots.robot import Robot

from collective_learning.aggregator.skill_aggregator \
    import SkillAggregator

from collective_learning.consensus.consensus_engine \
    import ConsensusEngine


robots = [
    Robot(f"robot-{i}")
    for i in range(10)
]

experiences = []

for robot in robots:

    for _ in range(100):

        experiences.append(
            robot.generate_experience()
        )

print()
print("Experiences Generated:")
print(len(experiences))

aggregator = SkillAggregator()

skills = aggregator.aggregate(
    experiences
)

print()
print("Discovered Strategies:")

for skill in skills:

    print(skill)

consensus = ConsensusEngine()

best = consensus.get_best_strategy(
    skills
)

print()
print("GLOBAL BEST STRATEGY")
print(best)

for robot in robots:

    robot.learn_skill(best)

print()
print("Distribution Complete")

for robot in robots:

    print(
        robot.robot_id,
        robot.learned_skills
    )
