from locust import HttpUser, task

class BankDemoUser(HttpUser):
    @task
    def BankDemo(self):
        self.client.get("/api/x3270")