from simulation.robots.robot import Robot


def test_robot_creation():

    robot = Robot("robot-1")

    assert robot.robot_id == "robot-1"


def test_skills_installation():

    robot = Robot("robot-1")

    robot.install_skill(
        {
            "name": "maze_navigation",
            "version": 1
        }
    )

    assert robot.get_skill_count() == 1


def test_skill_version_upgrade():

    robot = Robot("robot-1")

    robot.upgrade_skill(
        "maze_navigation",
        2
    )

    assert (
        robot.get_active_version(
            "maze_navigation"
        )
        == 2
    )