from fastapi import APIRouter

from backend.services.activity_service import (
    ActivityService
)


router = APIRouter()

service = ActivityService()


@router.get(
    "/dashboard/activity"
)
def get_activity():

    activities = (
        service.get_activities()
    )

    return {
        "count": len(activities),
        "activities": [
            {
                "id": item.id,
                "event_type":
                    item.event_type,
                "entity":
                    item.entity
            }
            for item in activities
        ]
    }