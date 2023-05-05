from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app import core

engine = create_engine(
    core.settings.MACARONDB_URL,
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
