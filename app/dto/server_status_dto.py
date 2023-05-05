from pydantic import BaseModel
from typing import Literal
from enum import Enum


class ServerStatusType(str, Enum):
    RUNNING = "Running"
    PENDING = "Pending"
    TERMINATING = "Terminating"
    DELETED = "Deleted"


class ServerStatus(BaseModel):
    status: ServerStatusType
