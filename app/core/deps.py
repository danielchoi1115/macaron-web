from typing import Generator


from app import core


async def get_db() -> Generator:
    try:
        db = core.db_session.SessionLocal()
        yield db
    finally:
        db.close()
