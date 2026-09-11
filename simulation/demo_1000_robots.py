from simulation.fleet import Fleet

fleet = Fleet(1000)

robots = fleet.get_robots()

print()

print(
    f"Network Size: {len(robots)}"
)
