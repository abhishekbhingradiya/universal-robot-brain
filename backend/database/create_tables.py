from backend.models.orm.base import (
    Base
)

from backend.models.orm.skill_model import (
    SkillModel
)

from backend.models.orm.robot_model import (
    RobotModel
)

from backend.models.orm.experience_model import (
    ExperienceModel
)

from backend.models.orm.federation_node_model import (
    FederationNodeModel
)

from backend.database.engine import (
    engine
)
from backend.models.orm.activity_model import (
    ActivityModel
)
from backend.models.orm.skill_history_model import (
    SkillHistoryModel
)
Base.metadata.create_all(
    bind=engine
)

print(
    "Tables created successfully"
)