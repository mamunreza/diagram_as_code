from diagrams import Diagram, Cluster, Edge
from diagrams.azure.integration import ServiceBus
from diagrams.k8s.compute import Pod

with Diagram(name="azure", filename="diagrams/azure", curvestyle="curved") as diagram:
    with Cluster("On-premise"):
        on_prem_app = Pod("On-premise .NET App")

    with Cluster("Azure"):
        service_bus = ServiceBus("Azure Service Bus")

    on_prem_app >> Edge(label="Consumes") << service_bus

