import networkx as nx


class KnowledgeGraph:

    def __init__(self):

        self.graph = nx.DiGraph()

    def add_robot(self, robot_id):

        self.graph.add_node(
            robot_id,
            type="robot"
        )

    def add_skill(
        self,
        skill_name
    ):

        self.graph.add_node(
            skill_name,
            type="skill"
        )

    def robot_learned_skill(
        self,
        robot_id,
        skill_name
    ):

        self.graph.add_edge(
            robot_id,
            skill_name,
            relation="learned"
        )

    def get_graph(self):

        return self.graph
