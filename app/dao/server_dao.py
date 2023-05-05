from sqlalchemy.orm import Session
from app import dto, entity
from .base_dao import BaseDAO


class ServerDao(BaseDAO[entity.ServerEntity, dto.Server, dto.Server]):
    def select(self, db: Session, *, dto: dto.Server):
        return (
            db.query(self.model)
            .filter(self.model.server_name == dto.server_name)
            .first()
        )

    def select_by_deployer(self, db: Session, *, dto: dto.Server):
        return (
            db.query(self.model)
            .filter(self.model.server_deployer == dto.server_deployer)
            .order_by(entity.ServerEntity.created_at.desc())
            .all()
        )

    def select_except_deployer(self, db: Session, *, dto: dto.Server):
        return (
            db.query(self.model)
            .filter(self.model.server_deployer != dto.server_deployer)
            .order_by(entity.ServerEntity.created_at.desc())
            .all()
        )

    def select_all(self, db: Session):
        return (
            db.query(self.model).order_by(entity.ServerEntity.created_at.desc()).all()
        )

    def insert(self, db: Session, *, dto: dto.Server):
        if not isinstance(dto, dict):
            dto = dto.dict(exclude_unset=True)
        db_obj = entity.ServerEntity(**dto)
        db.add(db_obj)
        return db_obj

    def delete(self, db: Session, *, dto: dto.Server):
        db_obj = self.select(db=db, dto=dto)
        db.delete(db_obj)
        return db_obj


server = ServerDao(entity.ServerEntity)
