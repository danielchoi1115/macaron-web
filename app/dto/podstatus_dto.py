from pydantic import BaseModel
from .server_status_dto import ServerStatusType


class PodStatus(BaseModel):
    name: str
    status: ServerStatusType

    class Config:
        orm_mode = True
