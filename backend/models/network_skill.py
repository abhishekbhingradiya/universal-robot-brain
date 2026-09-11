from pydantic import BaseModel


class NetworkSkill(BaseModel):

    skill_name: str
    strategy: str
    confidence: float
    origin_node: str