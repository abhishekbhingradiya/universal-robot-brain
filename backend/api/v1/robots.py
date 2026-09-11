from fastapi import (
    APIRouter,
    HTTPException
)

from pydantic import BaseModel

from backend.services.robot_service import (
    RobotService
)


router = APIRouter()

service = RobotService()


class RobotCreateRequest(
    BaseModel
):

    robot_id: str

    robot_type: str = "general"


@router.post("/robots")
def create_robot(
    request: RobotCreateRequest
):

    robot = service.register_robot(
        request.robot_id,
        request.robot_type
    )

    return {
        "id": robot.id,
        "robot_id": robot.robot_id,
        "robot_type": robot.robot_type,
        "status": robot.status
    }


@router.get("/robots")
def get_robots():

    robots = service.get_robots()

    return {
        "count": len(robots),
        "robots": [
            {
                "id": robot.id,
                "robot_id": robot.robot_id,
                "robot_type": robot.robot_type,
                "status": robot.status
            }
            for robot in robots
        ]
    }


@router.get("/robots/{robot_id}")
def get_robot(
    robot_id: str
):

    robot = service.get_robot(
        robot_id
    )

    if not robot:

        raise HTTPException(
            status_code=404,
            detail="Robot not found"
        )

    return {
        "id": robot.id,
        "robot_id": robot.robot_id,
        "robot_type": robot.robot_type,
        "status": robot.status
    }