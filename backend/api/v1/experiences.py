from fastapi import (
    APIRouter
)

from pydantic import (
    BaseModel
)

from backend.services.experience_service import (
    ExperienceService
)


router = APIRouter()

service = ExperienceService()


class ExperienceCreateRequest(
    BaseModel
):

    robot_id: str

    task: str

    strategy: str

    reward: float


@router.post(
    "/experiences"
)
def create_experience(
    request:
    ExperienceCreateRequest
):

    experience = (
        service.create_experience(
            request.robot_id,
            request.task,
            request.strategy,
            request.reward
        )
    )

    return {
        "id":
            experience.id,
        "robot_id":
            experience.robot_id,
        "task":
            experience.task,
        "strategy":
            experience.strategy,
        "reward":
            experience.reward
    }


@router.get(
    "/experiences"
)
def get_experiences():

    data = (
        service.get_experiences()
    )

    return {
        "count": len(data),
        "experiences": [
            {
                "id": item.id,
                "robot_id":
                    item.robot_id,
                "task":
                    item.task,
                "strategy":
                    item.strategy,
                "reward":
                    item.reward
            }
            for item in data
        ]
    }


@router.get(
    "/experiences/{robot_id}"
)
def get_robot_experiences(
    robot_id: str
):

    data = (
        service.get_robot_experiences(
            robot_id
        )
    )

    return {
        "robot_id":
            robot_id,
        "count":
            len(data),
        "experiences": [
            {
                "id": item.id,
                "task": item.task,
                "strategy":
                    item.strategy,
                "reward":
                    item.reward
            }
            for item in data
        ]
    }