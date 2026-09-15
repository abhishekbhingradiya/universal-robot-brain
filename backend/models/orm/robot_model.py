from sqlalchemy import (
    Integer,
    String
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column
)

from backend.models.orm.base import (
    Base
)


class RobotModel(Base):

    __tablename__ = "robots"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    robot_id: Mapped[str] = mapped_column(
        String(100),
        unique=True
    )

    status: Mapped[str] = mapped_column(
        String(50),
        default="active"
    )

    robot_type: Mapped[str] = mapped_column(
        String(100),
        default="general"
    )