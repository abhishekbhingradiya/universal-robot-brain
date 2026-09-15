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


class ActivityModel(Base):

    __tablename__ = "activities"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    event_type: Mapped[str] = mapped_column(
        String(100)
    )

    entity: Mapped[str] = mapped_column(
        String(100)
    )