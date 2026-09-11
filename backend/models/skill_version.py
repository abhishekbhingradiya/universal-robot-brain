from pydantic import BaseModel


class SkillVersion(BaseModel):

    skill_name: str
    version: int

    strategy: str

    fitness_score: float