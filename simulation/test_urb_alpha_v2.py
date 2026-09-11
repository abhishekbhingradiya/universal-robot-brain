from simulation.fleet import Fleet

from backend.services.fleet_upgrade \
    import FleetUpgrade


fleet = Fleet(100)

robots = fleet.get_robots()

skill_v1 = {
    "name": "maze_navigation",
    "version": 1,
    "fitness": 0.70
}

upgrader = FleetUpgrade()

count = upgrader.upgrade_fleet(
    robots,
    skill_v1
)

print(
    f"Installed V1 on {count} robots"
)

skill_v2 = {
    "name": "maze_navigation",
    "version": 2,
    "fitness": 0.84
}

count = upgrader.upgrade_fleet(
    robots,
    skill_v2
)

print(
    f"Upgraded V2 on {count} robots"
)