class GraphQueries:

    def get_skills_for_robot(
        self,
        graph,
        robot_id
    ):

        return list(
            graph.successors(
                robot_id
            )
        )