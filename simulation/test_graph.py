from intelligence_graph.graph import (
    KnowledgeGraph
)

kg = KnowledgeGraph()

kg.add_robot(
    "robot-1"
)

kg.add_skill(
    "maze_navigation"
)

kg.robot_learned_skill(
    "robot-1",
    "maze_navigation"
)

print(
    list(
        kg.get_graph().nodes()
    )
)

print(
    list(
        kg.get_graph().edges()
    )
)
