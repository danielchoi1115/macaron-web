from app import dto, core
import pykube
from typing import Type
from app.kubectl.kube_template_formatter import KubeTemplateFormatter
from .kube_parser import kubeParser


class KubeCTL:
    def __init__(self) -> None:
        kubeconfig = pykube.KubeConfig.from_file(core.settings.KUBECONFIG_PATH)
        self.api = pykube.HTTPClient(kubeconfig)

    def _create(self, api_object: Type[pykube.objects.APIObject], obj: dict):
        api_object(self.api, obj).create()

    def _delete(self, api_object: Type[pykube.objects.APIObject], obj: dict):
        api_object(self.api, obj).delete()

    def _create_combo(self, app: dto.KubeApp):
        self._create(pykube.Service, app.service_obj)
        self._create(pykube.Ingress, app.ingress_obj)
        self._create(pykube.Deployment, app.deployment_obj)

    def _delete_combo(self, app: dto.KubeApp):
        self._delete(pykube.Deployment, app.deployment_obj)
        self._delete(pykube.Ingress, app.ingress_obj)
        self._delete(pykube.Service, app.service_obj)

    def create_server(self, server: dto.Server):
        kubeTemplateFormatter = KubeTemplateFormatter(server=server)
        namespace = kubeTemplateFormatter.get_namespace_obj()
        flask = kubeTemplateFormatter.get_flask_kubeapp()
        mysql = kubeTemplateFormatter.get_mysql_kubeapp()

        self._create(pykube.Namespace, namespace)
        self._create_combo(flask)
        self._create_combo(mysql)

    def delete_server(self, server: dto.Server):
        kubeTemplateFormatter = KubeTemplateFormatter(server=server)
        namespace = kubeTemplateFormatter.get_namespace_obj()
        flask = kubeTemplateFormatter.get_flask_kubeapp()
        mysql = kubeTemplateFormatter.get_mysql_kubeapp()

        self._delete_combo(flask)
        self._delete_combo(mysql)
        self._delete(pykube.Namespace, namespace)

    def get_server_status(self, server: dto.Server):
        pods = pykube.objects.Pod.objects(self.api).filter(namespace=server.server_name)
        return kubeParser.parse_pods(pods)
