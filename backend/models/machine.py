from pydantic import BaseModel
from typing import List
from uuid import uuid4


class Machine(BaseModel):
    machine_id: str
    name: str
    machine_type: str
    capabilities: List[str]


def create_machine(name: str, machine_type: str):
    return Machine(
        machine_id=str(uuid4()),
        name=name,
        machine_type=machine_type,
        capabilities=[]
    )