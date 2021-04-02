from diagrams import Diagram, Cluster
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB
from diagrams.custom import Custom
from diagrams.onprem.database import MongoDB
from diagrams.onprem.analytics import Spark
from diagrams.onprem.analytics import Hadoop
from diagrams.onprem.workflow import Airflow
from diagrams.onprem.network import Internet
from diagrams.onprem.client import Client
from diagrams.onprem.client import Users
from diagrams.onprem.auth import Boundary
from diagrams.onprem.analytics import Tableau
from diagrams.oci.network import Firewall
from diagrams.oci.network import LoadBalancer
from diagrams.generic.network import Firewall

with Diagram("Data-As-Service API Architecture", show=False, filename="mingrammer_architecture", direction="LR"):
    users = Users("Uesrs")

    with Cluster("API Authentication"):
        firewall = Firewall("Authentication")
        accesstoken = Custom("Access Token", "./resources/accesstoken.png")
    
    with Cluster("API/Load Testing"):
        locust = Custom("Locust", "./resources/locust.png")
        pytest = Custom("Pytest", "./resources/pytest.png")
    with Cluster("Response/Request"):
        api = Custom("Fast API", "./resources/api.png")
        snowflakedb =  Custom("SnowflakeDB", "./resources/snowflakeDB.png")
    airflow = Airflow("Airflow")
    kaggle = Custom("Kaggle", "./resources/kaggle.png")

    users >> firewall
    firewall >> accesstoken >> firewall
    firewall >> api 
    api >> locust 
    api >> pytest 
    api >> snowflakedb >> api
    kaggle >> airflow >> snowflakedb