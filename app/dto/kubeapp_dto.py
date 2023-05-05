from pydantic import BaseModel


class KubeApp(BaseModel):
    service_obj: dict
    deployment_obj: dict
    ingress_obj: dict
