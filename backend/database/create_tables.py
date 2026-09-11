from backend.models.orm.base import (
    Base
)

from backend.models.orm.skill_model import (
    SkillModel
)

from backend.models.orm.robot_model import (
    RobotModel
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