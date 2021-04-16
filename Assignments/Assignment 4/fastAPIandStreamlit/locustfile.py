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
        self.client.get("http://127.0.0.1:8000/maskEntity?UserInput=NKE")
        self.client.get("http://127.0.0.1:8000/display_mask_entity?UserInput=AGEN")
        self.client.get("http://127.0.0.1:8000/replacePIIEntity?UserInput=AGEN")
        self.client.get("http://127.0.0.1:8000/Authentication?usrName=jayshil&usrPassword=jain")
        self.client.get("http://127.0.0.1:8000/deanonymize?user_input=NKE")
