class ConsensusEngine:

    def get_best_strategy(self, skills):

        return sorted(
            skills,
            key=lambda x:
            x["avg_reward"],
            reverse=True
        )[0]
