import os

from dotenv import load_dotenv


load_dotenv()


class Settings:

    def __init__(self):

        self.ENV = os.getenv(
            "URB_ENV",
            "development"
        )

        self.DATABASE_URL = os.getenv(
            "DATABASE_URL",
            "sqlite:///urb_network.db"
        )

        self.LOG_LEVEL = os.getenv(
            "LOG_LEVEL",
            "INFO"
        )

        self.NETWORK_NAME = os.getenv(
            "NETWORK_NAME",
            "UniversalRobotBrain"
        )

        self.MAX_ROBOTS = int(
            os.getenv(
                "MAX_ROBOTS",
                100000
            )
        )


settings = Settings()