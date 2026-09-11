from simulation.fleet import Fleet

from simulation.evolution_cycle \
    import EvolutionCycle


fleet = Fleet(100)

robots = fleet.get_robots()

all_experiences = []

for robot in robots:

    for _ in range(100):

        all_experiences.append(
            robot.generate_experience()
        )

print()

print(
    "Generated Experiences:"
)

print(
    len(all_experiences)
)

cycle = EvolutionCycle()

best_skill = cycle.run(
    all_experiences
)

print()

print(
    "Best Skill Found:"
)

print(best_skill)

for robot in robots:

    robot.install_skill(
        best_skill
    )

print()

print(
    f"Installed on {len(robots)} robots"
)