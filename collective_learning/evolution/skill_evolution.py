class SkillEvolution:

    def evolve(
            self,
            current_skill,
            new_strategy):

        if (
            new_strategy["average_reward"]
            >
            current_skill["average_reward"]
        ):
            return new_strategy

        return current_skill