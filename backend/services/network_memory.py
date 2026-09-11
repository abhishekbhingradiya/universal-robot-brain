from backend.database.db import get_connection

from backend.logger import logger


def save_global_skill(skill):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO global_skills
        (strategy, avg_reward)
        VALUES (?, ?)
        """,
        (
            skill["strategy"],
            skill["avg_reward"]
        )
    )

    conn.commit()

    conn.close()

    logger.info(
        f"Saved global skill: "
        f"{skill['strategy']} "
        f"(reward={skill['avg_reward']})"
    )


def get_global_skills():

    conn = get_connection()

    cursor = conn.cursor()

    rows = cursor.execute(
        """
        SELECT strategy,
               avg_reward
        FROM global_skills
        """
    ).fetchall()

    conn.close()

    logger.info(
        f"Loaded {len(rows)} global skills"
    )

    return rows