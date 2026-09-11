from sqlalchemy.orm import sessionmaker

from backend.database.engine import (
    engine
)

SessionLocal = sessionmaker(
    bind=engine,
    expire_on_commit=False
)