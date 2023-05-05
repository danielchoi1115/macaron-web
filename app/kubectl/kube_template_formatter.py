from app.kubectl.kube_templates import flask_template, mysql_template, common_templates
from app import dto


class KubeTemplateFormatter:
    def __init__(self, server: dto.Server) -> None:
        self.server = server

    def set_namespace(self, template: dict):
        template["metadata"]["namespace"] = self.server.server_name

    def format_flask_deployment(self):
        tp = flask_template.deployment()
        self.set_namespace(tp)
        image = f"danielchoi1115/macaron-flask-demo:{self.server.game_server_tag}"
        tp["spec"]["template"]["spec"]["containers"][0]["image"] = image
        return tp

    def format_flask_service(self):
        tp = flask_template.service()
        self.set_namespace(tp)
        return tp

    def format_flask_ingress(self):
        tp = flask_template.ingress()
        self.set_namespace(tp)
        host = f"{self.server.server_name}.ginger-macaron.world"
        tp["spec"]["rules"][0]["host"] = host
        return tp

    def format_mysql_deployment(self):
        tp = mysql_template.deployment()
        self.set_namespace(tp)
        image = f"danielchoi1115/macaron-mysql-demo:{self.server.macaron_tag}"
        tp["spec"]["template"]["spec"]["containers"][0]["image"] = image
        return tp

    def format_mysql_service(self):
        tp = mysql_template.service()
        self.set_namespace(tp)
        return tp

    def format_mysql_ingress(self):
        tp = mysql_template.ingress()
        self.set_namespace(tp)
        host = f"{self.server.server_name}-db.ginger-macaron.world"
        tp["spec"]["rules"][0]["host"] = host
        return tp

    def get_namespace_obj(self):
        tp = common_templates.namespace()
        tp["metadata"]["name"] = self.server.server_name
        return tp

    def get_flask_kubeapp(self) -> dto.KubeApp:
        return dto.KubeApp(
            service_obj=self.format_flask_service(),
            deployment_obj=self.format_flask_deployment(),
            ingress_obj=self.format_flask_ingress(),
        )

    def get_mysql_kubeapp(self) -> dto.KubeApp:
        return dto.KubeApp(
            service_obj=self.format_mysql_service(),
            deployment_obj=self.format_mysql_deployment(),
            ingress_obj=self.format_mysql_ingress(),
        )
