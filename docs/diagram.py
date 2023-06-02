#!/usr/bin/env python3
import os

from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.compute import GKE
from diagrams.gcp.network import LoadBalancing
from diagrams.k8s.compute import Pod
from diagrams.k8s.network import Service, Ingress
from diagrams.onprem.client import Users
from diagrams.onprem.vcs import Github

graph_attr = {
    "splines": "spline",  # rounded arrows, much nicer
}

with Diagram('devi-revolutti Architecture with GKE and GHA',
             direction='TB',
             filename='architecture',
             graph_attr=graph_attr,
             ):
    users = Users("Internet Users")
    developers = Users("Developers")
    github = Github("GitHub Actions")

    developers >> github

    with Cluster("Google Cloud"):
        load_balancer = LoadBalancing("Cloud Load Balancer")

        users >> load_balancer

        with Cluster("Kubernetes Cluster"):
            gcp = GKE("GKE")

            with Cluster("Ingress"):
                ingress = Ingress("Kubernetes Ingress")

            with Cluster("PythonApp"):
                service_python = Service("PythonApp Service")
                ingress >> service_python
                pods = []
                for _ in range(1, 4, 1):
                    pods.append(service_python >> Pod(f"PythonApp {_}"))

            with Cluster("MySQL"):
                service_db = Service("MySQL Service")
                pods = [Pod(f"Primary {_}"), Pod(f"Secondary {_}")]
                service_db >> pods

            service_python >> service_db
            load_balancer >> ingress

            github >> Edge(label="helm upgrade", style="dashed") >> service_python
