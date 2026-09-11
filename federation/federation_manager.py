class FederationManager:

    def __init__(self):

        self.nodes = []

    def register(
        self,
        node
    ):
        self.nodes.append(node)

    def list_nodes(self):

        return self.nodes
