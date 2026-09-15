from backend.services.robot_service import (
    RobotService
)

from backend.services.experience_service import (
    ExperienceService
)

from backend.services.federation_service import (
    FederationService
)

from backend.services.network_memory import (
    get_global_skills
)


class GraphService:

    def __init__(self):

        self.robot_service = (
            RobotService()
        )

        self.experience_service = (
            ExperienceService()
        )

        self.federation_service = (
            FederationService()
        )

    def build_graph(self):

        nodes = []

        edges = []

        robots = (
            self.robot_service.get_robots()
        )

        skills = (
            get_global_skills()
        )

        experiences = (
            self.experience_service
            .get_experiences()
        )

        federation_nodes = (
            self.federation_service
            .get_nodes()
        )

        # Robots

        for robot in robots:

            nodes.append(
                {
                    "id":
                        robot.robot_id,
                    "type":
                        "robot"
                }
            )

        # Skills

        for skill in skills:

            nodes.append(
                {
                    "id":
                        skill[0],
                    "type":
                        "skill"
                }
            )

        # Federation

        for node in federation_nodes:

            nodes.append(
                {
                    "id":
                        node.node_id,
                    "type":
                        "federation"
                }
            )

        # Experience Relationships

        for exp in experiences:

            edges.append(
                {
                    "source":
                        exp.robot_id,
                    "target":
                        exp.strategy,
                    "relationship":
                        "generated"
                }
            )

        # Federation Relationships

        if federation_nodes:

            node_id = (
                federation_nodes[0]
                .node_id
            )

            for robot in robots:

                edges.append(
                    {
                        "source":
                            node_id,
                        "target":
                            robot.robot_id,
                        "relationship":
                            "hosts"
                    }
                )

        return {
            "nodes":
                nodes,
            "edges":
                edges
        }