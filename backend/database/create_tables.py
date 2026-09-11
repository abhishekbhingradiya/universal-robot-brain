from backend.models.orm.base import (
    Base
)

from backend.models.orm.skill_model import (
    SkillModel
)

from backend.database.engine import (
    engine
)


Base.metadata.create_all(
    bind=engine
)

print(
    "Tables created successfully"
)