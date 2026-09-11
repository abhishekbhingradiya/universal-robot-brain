from backend.services.robot_service import (
    RobotService
)

service = RobotService()

service.register_robot(
    "robot-001",
    "explorer"
)

service.register_robot(
    "robot-002",
    "worker"
)

robots = service.get_robots()

print()

for robot in robots:

    print(
        robot.robot_id,
        robot.robot_type,
        robot.status
    )