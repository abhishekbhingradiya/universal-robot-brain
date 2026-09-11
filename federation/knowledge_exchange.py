from backend.logger import logger


class KnowledgeExchange:

    def transfer(
        self,
        source,
        target
    ):

        transferred_count = 0

        for item in source.get_knowledge():

            target.publish_knowledge(
                item
            )

            transferred_count += 1

        logger.info(
            f"Transferred "
            f"{transferred_count} knowledge items "
            f"from {source.node_id} "
            f"to {target.node_id}"
        )

        return transferred_count