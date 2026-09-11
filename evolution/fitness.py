class FitnessCalculator:

    def calculate(
        self,
        rewards
    ):

        if not rewards:
            return 0

        return sum(
            rewards
        ) / len(
            rewards
        )