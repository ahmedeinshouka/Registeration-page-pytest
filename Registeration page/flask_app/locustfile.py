from locust import HttpUser, between, task

class WebsiteUser(HttpUser):
    wait_time = between(5, 9)

    @task
    def test_registration(self):
        self.client.post('/register', json={
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'password'
        })

    @task
    def test_home_page(self):
        self.client.get('/')

