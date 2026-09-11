from evolution.evolution_engine import (
    EvolutionEngine
)

current_skill = {
    "skill": "maze_navigation",
    "version": 1,
    "fitness": 0.70
}

candidate_skill = {
    "fitness": 0.84
}

engine = EvolutionEngine()

result = engine.evolve(
    current_skill,
    candidate_skill
)

print(result)