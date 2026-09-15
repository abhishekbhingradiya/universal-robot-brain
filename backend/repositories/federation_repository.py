from backend.database.session import (
    SessionLocal
)

from backend.models.orm.federation_node_model import (
    FederationNodeModel
)

from backend.logger import logger


class FederationRepository:

    def create(
        self,
        node_id,
        region
    ):

        session = SessionLocal()

        try:

            existing = (
                session.query(
                    FederationNodeModel
                )
                .filter(
                    FederationNodeModel.node_id
                    == node_id
                )
                .first()
            )

            if existing:

                logger.info(
                    f"Federation node already exists: {node_id}"
                )

                return existing

            node = FederationNodeModel(
                node_id=node_id,
                region=region,
                status="active"
            )

            session.add(node)

            session.commit()

            logger.info(
                f"Federation node created: {node_id}"
            )

            return node

        finally:

            session.close()

    def get_all(self):

        session = SessionLocal()

        try:

            return (
                session.query(
                    FederationNodeModel
                )
                .all()
            )

        finally:

            session.close()

    def count(self):

        session = SessionLocal()

        try:

            return (
                session.query(
                    FederationNodeModel
                )
                .count()
            )

        finally:

            session.close()