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


class SkillHistoryModel(Base):

    __tablename__ = "skill_history"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    skill_name: Mapped[str] = mapped_column(
        String(100)
    )

    version: Mapped[int] = mapped_column(
        Integer
    )

    fitness: Mapped[float] = mapped_column(
        Float
    )