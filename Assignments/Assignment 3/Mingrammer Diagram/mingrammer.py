from diagrams import Diagram, Cluster
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB
from diagrams.custom import Custom
from diagrams.onprem.database import MongoDB
from diagrams.onprem.analytics import Spark
from diagrams.onprem.analytics import Hadoop
#from diagrams.programming.framework.Fastapi import FastAPI
#diagrams.onprem.client.Client

with Diagram("Moody Analytics API", show=False, filename="mingrammer", direction="LR"):
    #ELB("lb") >> EC2("web") >> RDS("userdb")
    api = Custom("API", "./resources/api.png")
    users = Custom("Users", "./resources/users.png")
    firewall = Custom("Firewall", "./resources/firewall.png")
    website = Custom("Website", "./resources/website.png")
    data_service = Custom("Dataservice", "./resources/data_service.png")
    mongodb = MongoDB("Configuration")
    spark = Spark("Apache Spark")
    hadoop = Hadoop("HDFS/Parquet")
    audit = Custom("Audit", "./resources/audit.png")
    
    # with Cluster("Service Cluster"):
    #     service_cluster = [
    #         mongodb("Configuration"),
    #         data_service("Data Services"),
    #         spark("Apache Spark")]

    api >> firewall 
    users >> firewall
    firewall >> website 
    website >> data_service
    data_service >> mongodb 
    data_service >> spark
    spark >> hadoop
    mongodb >> audit
