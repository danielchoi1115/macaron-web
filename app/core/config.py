from pydantic import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"

    MACARONDB_URL = (
        "mysql+mysqlconnector://macaron:macaron@10.111.105.34:43306/macarondb"
    )
    KUBECONFIG_PATH = "/root/.kube/config"


@lru_cache
def get_settings():
    return Settings()


settings = get_settings()
