from backend.models.skill import create_skill


def knowledge_to_skill(knowledge):

    return create_skill(
        name=f"{knowledge['task']}_mastery",
        task=knowledge["task"],
        confidence=knowledge["confidence"],
        source_machines=["shared-network"]
    )