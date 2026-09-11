from fastapi import APIRouter

router = APIRouter()

skills = []


@router.get("/")
def get_skills():

    return skills


@router.post("/")
def publish_skill(skill: dict):

    skills.append(skill)

    return {
        "message": "skill published",
        "count": len(skills)
    }