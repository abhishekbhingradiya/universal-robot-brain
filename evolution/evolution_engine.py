from evolution.version_manager import (
    VersionManager
)


class EvolutionEngine:

    def evolve(
        self,
        current_skill,
        candidate_skill
    ):

        if (
            candidate_skill[
                "fitness"
            ]
            >
            current_skill[
                "fitness"
            ]
        ):

            vm = VersionManager()

            return {
                "skill":
                    current_skill[
                        "skill"
                    ],
                "version":
                    vm.next_version(
                        current_skill[
                            "version"
                        ]
                    ),
                "fitness":
                    candidate_skill[
                        "fitness"
                    ]
            }

        return current_skill