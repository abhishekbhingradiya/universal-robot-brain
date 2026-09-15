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


class FederationNodeModel(Base):

    __tablename__ = "federation_nodes"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    node_id: Mapped[str] = mapped_column(
        String(100),
        unique=True
    )

    region: Mapped[str] = mapped_column(
        String(100)
    )

    status: Mapped[str] = mapped_column(
        String(50),
        default="active"
    )
