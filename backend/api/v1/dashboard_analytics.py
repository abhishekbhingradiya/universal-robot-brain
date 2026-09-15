from fastapi import APIRouter

from backend.services.network_memory import (
    get_global_skills
)

from backend.services.activity_service import (
    ActivityService
)


router = APIRouter()

activity_service = ActivityService()


@router.get(
    "/dashboard/top-skills"
)
def top_skills():

    skills = get_global_skills()

    sorted_skills = sorted(
        skills,
        key=lambda x: x[1],
        reverse=True
    )

    return {
        "count": len(sorted_skills),
        "skills": [
            {
                "strategy": item[0],
                "avg_reward": item[1]
            }
            for item in sorted_skills
        ]
    }


@router.get(
    "/dashboard/recent-activity"
)
def recent_activity():

    activities = (
        activity_service
        .get_activities()
    )

    return {
        "count": len(activities),
        "activities": [
            {
                "id": item.id,
                "event_type": item.event_type,
                "entity": item.entity
            }
            for item in activities[:20]
        ]
    }


@router.get(
    "/dashboard/network-health"
)
def network_health():

    skills = get_global_skills()

    return {
        "status": "healthy",
        "skills_available":
            len(skills)
    }