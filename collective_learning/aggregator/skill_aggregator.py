from collections import defaultdict


class SkillAggregator:

    def aggregate(self, experiences):

        grouped = defaultdict(list)

        for exp in experiences:

            grouped[
                exp["strategy"]
            ].append(
                exp["reward"]
            )

        results = []

        for strategy, rewards in grouped.items():

            results.append({
                "strategy": strategy,
                "avg_reward":
                    sum(rewards) / len(rewards)
            })

        return results