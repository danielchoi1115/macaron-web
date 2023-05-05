from typing import Generic, Type, TypeVar
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app import entity

ModelType = TypeVar("ModelType", bound=entity.Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class BaseDAO(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    def commit(self, db: Session):
        db.commit()
