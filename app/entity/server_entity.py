from sqlalchemy import Column, String, TIMESTAMP
from sqlalchemy.dialects.mysql import INTEGER
from app.entity.base_entity import Base


class ServerEntity(Base):
    __tablename__ = "servers"
    server_id = Column(INTEGER(unsigned=True), primary_key=True, index=True)
    server_name = Column(String(200), unique=True, nullable=False)
    description = Column(String(200), nullable=False)
    server_deployer = Column(String(200), nullable=False)
    game_server_tag = Column(String(50), nullable=False)
    macaron_tag = Column(String(50), nullable=False)
    created_at = Column(TIMESTAMP, server_default="CURRENT_TIMESTAMP")
