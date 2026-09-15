from fastapi import APIRouter

from pydantic import BaseModel

from backend.services.federation_service import (
    FederationService
)


router = APIRouter()

service = FederationService()


class FederationNodeRequest(
    BaseModel
):

    node_id: str

    region: str


@router.post(
    "/federation/nodes"
)
def create_node(
    request: FederationNodeRequest
):

    node = service.create_node(
        request.node_id,
        request.region
    )

    return {
        "id": node.id,
        "node_id": node.node_id,
        "region": node.region,
        "status": node.status
    }


@router.get(
    "/federation/nodes"
)
def get_nodes():

    nodes = service.get_nodes()

    return {
        "count": len(nodes),
        "nodes": [
            {
                "id": node.id,
                "node_id": node.node_id,
                "region": node.region,
                "status": node.status
            }
            for node in nodes
        ]
    }