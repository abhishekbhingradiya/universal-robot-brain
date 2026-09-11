from sqlalchemy.orm import sessionmaker

from backend.database.engine import (
    engine
)

SessionLocal = sessionmaker(
    bind=engine
)