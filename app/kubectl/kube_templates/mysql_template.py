def deployment():
    return {
        "apiVersion": "apps/v1",
        "kind": "Deployment",
        "metadata": {"name": "deploy2-mysql", "namespace": None},
        "spec": {
            "replicas": 1,
            "selector": {"matchLabels": {"app": "deploy2-mysql"}},
            "template": {
                "metadata": {"labels": {"app": "deploy2-mysql"}},
                "spec": {
                    "containers": [
                        {
                            "name": "pod-mysql",
                            "image": None,
                            "env": [
                                {"name": "MYSQL_ROOT_PASSWORD", "value": "password"}
                            ],
                            "ports": [{"containerPort": 3306}],
                            "resources": {
                                "limits": {"memory": "500Mi", "cpu": "500m"},
                                "requests": {"memory": "250Mi", "cpu": "250m"},
                            },
                        },
                        {
                            "name": "adminer",
                            "image": "adminer:4.8.1",
                            "ports": [{"containerPort": 8080}],
                            "env": [{"name": "ADMINER_DESIGN", "value": "pappu687"}],
                        },
                    ]
                },
            },
        },
    }


def service():
    return {
        "apiVersion": "v1",
        "kind": "Service",
        "metadata": {"name": "db", "namespace": None},
        "spec": {
            "type": "NodePort",
            "selector": {"app": "deploy2-mysql"},
            "ports": [
                {"name": "mysql-port", "port": 3306, "targetPort": 3306},
                {"name": "adminer-port", "port": 43306, "targetPort": 8080},
            ],
        },
    }


def ingress():
    return {
        "apiVersion": "networking.k8s.io/v1",
        "kind": "Ingress",
        "metadata": {"name": "mysql-ingress", "namespace": None},
        "spec": {
            "ingressClassName": "nginx",
            "rules": [
                {
                    "host": None,
                    "http": {
                        "paths": [
                            {
                                "path": "/",
                                "pathType": "Prefix",
                                "backend": {
                                    "service": {"name": "db", "port": {"number": 43306}}
                                },
                            }
                        ]
                    },
                }
            ],
        },
    }
