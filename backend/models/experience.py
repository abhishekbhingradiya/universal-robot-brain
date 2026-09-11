from pydantic import BaseModel


class Experience(BaseModel):
    machine_id: str
    task: str
    strategy: str
    success: bool
    reward: float