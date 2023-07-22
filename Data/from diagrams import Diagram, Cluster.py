from diagrams import Diagram, Cluster
from diagrams.azure.compute import AKS
from diagrams.azure.integration import APIManagement
from diagrams.azure.database import CosmosDb
from diagrams.azure.general import Userprivacy
from diagrams.onprem.client import User
from diagrams.onprem.queue import Kafka
from diagrams.saas.chat import Slack
from diagrams.generic.network import Firewall

with Diagram("E-Commerce Deployment Diagram", show=True):
    user = User("Customer")

    with Cluster("Azure Cloud"):
        with Cluster("Microservices"):
            user_service = AKS("User Service")
            product_service = AKS("Product Service")
            order_service = AKS("Order Service")
            payment_service = AKS("Payment Service")
            notification_service = AKS("Notification Service")
        
        api_gateway = APIManagement("API Gateway")
        message_broker = Kafka("Kafka Message Broker")
        db = CosmosDb("Cosmos DB")
        gdpr = Privacy("Privacy & Compliance (GDPR)")
        payment_gateway = Firewall("Payment Gateway (PCI DSS)")

        user >> api_gateway >> user_service
        user >> api_gateway >> product_service
        user >> api_gateway >> order_service
        user >> api_gateway >> payment_service >> payment_gateway
        user >> api_gateway >> notification_service

        user_service >> db
        product_service >> db
        order_service >> db
        payment_service >> db
        notification_service >> db

        user_service >> message_broker
        product_service >> message_broker
        order_service >> message_broker
        payment_service >> message_broker
        notification_service >> message_broker

        user_service >> gdpr
        product_service >> gdpr
        order_service >> gdpr
        payment_service >> gdpr
        notification_service >> gdpr
