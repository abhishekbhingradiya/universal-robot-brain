from pydantic import BaseModel


class Knowledge(BaseModel):
    task: str
    best_strategy: str
    confidence: float