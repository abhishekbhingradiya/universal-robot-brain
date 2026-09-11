from collective_learning.aggregator.skill_aggregator\
 import SkillAggregator

from collective_learning.consensus.consensus_engine\
 import ConsensusEngine


class EvolutionCycle:

    def run(
        self,
        experiences
    ):

        aggregator = SkillAggregator()

        results = aggregator.aggregate(
            experiences
        )

        consensus = ConsensusEngine()

        best = consensus.get_best_strategy(
            results
        )

        return best