from backend.services.skill_history_service import (
    SkillHistoryService
)

service = SkillHistoryService()

service.record_version(
    "left_wall",
    1,
    0.70
)

service.record_version(
    "left_wall",
    2,
    0.84
)

service.record_version(
    "left_wall",
    3,
    0.91
)

print(
    "Timeline data created"
)