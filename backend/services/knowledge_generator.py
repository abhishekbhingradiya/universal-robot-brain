from collections import defaultdict


def extract_knowledge(experiences):

    stats = defaultdict(list)

    for exp in experiences:
        if exp.success:
            stats[exp.task].append(exp.strategy)

    knowledge = []

    for task, strategies in stats.items():

        strategy_count = {}

        for s in strategies:
            strategy_count[s] = strategy_count.get(s, 0) + 1

        best = max(strategy_count, key=strategy_count.get)

        knowledge.append({
            "task": task,
            "best_strategy": best,
            "confidence": strategy_count[best] / len(strategies)
        })

    return knowledge