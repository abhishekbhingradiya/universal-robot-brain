from pydantic import BaseModel
from typing import List
from uuid import uuid4


class Skill(BaseModel):

    skill_id: str
    name: str
    task: str
    confidence: float
    source_machines: List[str]


def create_skill(
        name,
        task,
        confidence,
        source_machines):

    return Skill(
        skill_id=str(uuid4()),
        name=name,
        task=task,
        confidence=confidence,
        source_machines=source_machines
    )