class SkillLineage:

    def __init__(self):

        self.history = {}

    def add_version(
        self,
        skill,
        version
    ):

        if skill not in self.history:
            self.history[skill] = []

        self.history[
            skill
        ].append(
            version
        )

    def get_history(
        self,
        skill
    ):

        return self.history.get(
            skill,
            []
        )