class KnowledgeExchange:

    def transfer(
        self,
        source,
        target
    ):

        for item in source.get_knowledge():

            target.publish_knowledge(
                item
            )