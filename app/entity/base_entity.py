from typing import Dict
from sqlalchemy.ext.declarative import as_declarative

class_registry: Dict = {}


@as_declarative(class_registry=class_registry)
class Base:
    ...
