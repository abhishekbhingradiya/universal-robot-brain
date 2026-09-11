from backend.logger import logger


class FederationNode:

    def __init__(
        self,
        node_id,
        region
    ):

        self.node_id = node_id

        self.region = region

        self.knowledge = []

        logger.info(
            f"Federation node created: "
            f"{node_id} ({region})"
        )

    def publish_knowledge(
        self,
        knowledge
    ):

        self.knowledge.append(
            knowledge
        )

        logger.info(
            f"{self.node_id} "
            f"published knowledge"
        )

    def get_knowledge(
        self
    ):

        return self.knowledge