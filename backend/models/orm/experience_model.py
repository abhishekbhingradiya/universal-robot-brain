from sqlalchemy import (
    Integer,
    String,
    Float
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column
)

from backend.models.orm.base import (
    Base
)


class ExperienceModel(Base):

    __tablename__ = "experiences"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    robot_id: Mapped[str] = mapped_column(
        String(100)
    )

    task: Mapped[str] = mapped_column(
        String(100)
    )

    strategy: Mapped[str] = mapped_column(
        String(100)
    )

    reward: Mapped[float] = mapped_column(
        Float
    )