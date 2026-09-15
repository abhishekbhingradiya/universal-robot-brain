from fastapi import APIRouter

from backend.services.graph_service import (
    GraphService
)

router = APIRouter()

graph_service = (
    GraphService()
)


@router.get(
    "/network/graph"
)
def network_graph():

    return (
        graph_service
        .build_graph()
    )