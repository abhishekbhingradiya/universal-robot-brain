from backend.services.network_memory import (
    save_global_skill,
    get_global_skills
)

save_global_skill(
    {
        "strategy": "left_wall",
        "avg_reward": 0.71
    }
)

skills = get_global_skills()

print()

print("Network Memory")

for skill in skills:

    print(skill)