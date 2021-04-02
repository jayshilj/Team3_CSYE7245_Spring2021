# locust -f locustfile.py
from locust import HttpUser, between, task


class WebsiteUser(HttpUser):
    wait_time = between(5, 15)
    
    def on_start(self):
        self.client.post("/login", {
            "username": "test_user",
            "password": ""
        })
    
    @task
    def index(self):
        # self.client.get("/")
        # self.client.get("/static/assets.js")
        self.client.get("http://localtest.me:8000/getexpcnc/3")
        self.client.get("http://localtest.me:8000/getexperimentdatamachine/2/Prep")
        self.client.get("http://localtest.me:8000/knowexpmachiningfinalized/yes")
        self.client.get("http://localtest.me:8000/getdatamachiningfinalized/no")
        self.client.get("http://localtest.me:8000/knowexpwornstatus/worn")
        self.client.get("http://localtest.me:8000/getdatatool/worn")
        
        
    # @task
    # def about(self):
    #     self.client.get("/about/")

    # @task
    # def about(self):
    #     self.client.get("http://localtest.me:8000/getexpcnc/3")

    # @task
    # def about(self):
    #     self.client.get("http://localtest.me:8000/getexperimentdatamachine/2/Prep")

    # @task
    # def about(self):
    #     self.client.get("http://localtest.me:8000/knowexpwornstatus/worn")


    # @task
    # def about(self):
    #     self.client.get("http://localtest.me:8000/getdatatool/worn")

    # @task
    # def about(self):
    #     self.client.get("http://localtest.me:8000/knowexppassvisual/no")

    # @task
    # def about(self):
    #     self.client.get("http://localtest.me:8000/getdatavisualinspection/no")

    
    # @task
    # def about(self):
    #     self.client.get("http://localtest.me:8000/knowexpmachiningfinalized/yes")

    
    # @task
    # def about(self):
    #     self.client.get("http://localtest.me:8000/getdatamachiningfinalized/no")



