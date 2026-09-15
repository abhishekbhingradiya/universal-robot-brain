from backend.repositories.federation_repository import (
    FederationRepository
)

from backend.services.activity_service import (
    ActivityService
)


class FederationService:

    def __init__(self):

        self.repo = FederationRepository()

        self.activity_service = (
            ActivityService()
        )

    def create_node(
        self,
        node_id,
        region
    ):

        node = self.repo.create(
            node_id,
            region
        )

        self.activity_service.log_federation_created(
            node_id
        )

        return node

    def get_nodes(self):

        return self.repo.get_all()

    def get_node_count(self):

        return self.repo.count()