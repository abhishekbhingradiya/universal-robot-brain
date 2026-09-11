def recommend_skill(
        available_skills,
        task):

    matching = [
        s
        for s in available_skills
        if s.task == task
    ]

    if not matching:
        return None

    return sorted(
        matching,
        key=lambda x: x.confidence,
        reverse=True
    )[0]