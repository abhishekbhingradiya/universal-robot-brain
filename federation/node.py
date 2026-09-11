class FederationNode:

    def __init__(
        self,
        node_id,
        region
    ):
        self.node_id = node_id
        self.region = region
        self.knowledge = []

    def publish_knowledge(
        self,
        knowledge
    ):
        self.knowledge.append(
            knowledge
        )

    def get_knowledge(self):
        return self.knowledge