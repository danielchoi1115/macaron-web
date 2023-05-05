from app import dto, kubectl


class KubeService:
    def __init__(self) -> None:
        self.kubectl = kubectl.KubeCTL()

    def get_server_status(self, server: dto.Server) -> dto.ServerStatusType:
        podStatusList = self.kubectl.get_server_status(server)

        status = dto.ServerStatusType.RUNNING

        if not podStatusList:
            status = dto.ServerStatusType.DELETED

        for pod in podStatusList:
            if pod.status != dto.ServerStatusType.RUNNING:
                status = pod.status
                break

        return dto.ServerStatus(status=status)

    def create(self, server: dto.Server):
        self.kubectl.create_server(server)

    def delete(self, server: dto.Server):
        self.kubectl.delete_server(server)


kube = KubeService()

# bq = ks.get(Server)
