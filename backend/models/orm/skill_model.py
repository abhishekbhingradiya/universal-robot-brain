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


class SkillModel(Base):

    __tablename__ = "skills"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    strategy: Mapped[str] = mapped_column(
        String(100)
    )

    avg_reward: Mapped[float] = mapped_column(
        Float
    )