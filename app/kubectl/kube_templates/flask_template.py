def deployment():
    return {
        "apiVersion": "apps/v1",
        "kind": "Deployment",
        "metadata": {"name": "deploy1-flasksrv", "namespace": None},
        "spec": {
            "replicas": 1,
            "selector": {"matchLabels": {"app": "deploy1-flasksrv"}},
            "template": {
                "metadata": {"labels": {"app": "deploy1-flasksrv"}},
                "spec": {
                    "containers": [
                        {
                            "name": "pod-flask",
                            "image": None,
                            "workingDir": "/app",
                            "ports": [{"containerPort": 40080}],
                            "resources": {
                                "limits": {"memory": "500Mi", "cpu": "500m"},
                                "requests": {"memory": "250Mi", "cpu": "250m"},
                            },
                        }
                    ]
                },
            },
        },
    }


def service():
    return {
        "apiVersion": "v1",
        "kind": "Service",
        "metadata": {"name": "flasksrv", "namespace": None},
        "spec": {
            "type": "NodePort",
            "selector": {"app": "deploy1-flasksrv"},
            "ports": [{"name": "flask-port", "port": 50080, "targetPort": 40080}],
        },
    }


def ingress():
    return {
        "apiVersion": "networking.k8s.io/v1",
        "kind": "Ingress",
        "metadata": {
            "name": "flask-ingress",
            "namespace": None,
            "annotations": {"nginx.ingress.kubernetes.io/rewrite-target": "/$1"},
        },
        "spec": {
            "ingressClassName": "nginx",
            "rules": [
                {
                    "host": None,
                    "http": {
                        "paths": [
                            {
                                "path": "/?(.*)",
                                "pathType": "Prefix",
                                "backend": {
                                    "service": {
                                        "name": "flasksrv",
                                        "port": {"number": 50080},
                                    }
                                },
                            }
                        ]
                    },
                }
            ],
        },
    }
