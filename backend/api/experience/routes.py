from fastapi import APIRouter
from backend.models.experience import Experience

router = APIRouter()

experiences = []

@router.post("/")
def upload_experience(exp: Experience):
    experiences.append(exp)
    return {
        "message": "experience stored",
        "count": len(experiences)
    }


@router.get("/")
def get_experiences():
    return experiences