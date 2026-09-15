from backend.repositories.federation_repository import (
    FederationRepository
)


class FederationService:

    def __init__(self):

        self.repo = FederationRepository()

    def create_node(
        self,
        node_id,
        region
    ):

        return self.repo.create(
            node_id,
            region
        )

    def get_nodes(self):

        return self.repo.get_all()

    def get_node_count(self):

        return self.repo.count()