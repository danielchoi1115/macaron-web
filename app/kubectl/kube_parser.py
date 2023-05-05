from typing import Iterable, List
from app import dto
import pykube


class KubeParser:
    @staticmethod
    def parse_pods(pods: Iterable[pykube.objects.Pod]) -> List[dto.PodStatus]:
        podStatusList = []
        for pod in pods:
            if (
                pod.obj["status"].get("phase") == "Running"
                and pod.obj["metadata"].get("deletionTimestamp") is not None
            ):
                status = dto.ServerStatusType.TERMINATING
            elif pod.obj["status"].get("phase") in ("Succeeded", "Failed"):
                status = dto.ServerStatusType.TERMINATING
            elif pod.obj["status"].get("phase") == "Pending":
                status = dto.ServerStatusType.PENDING
            else:
                status = dto.ServerStatusType.RUNNING

            podStatus = dto.PodStatus(name=pod.labels["app"], status=status)

            podStatusList.append(podStatus)
        return podStatusList


kubeParser = KubeParser()
