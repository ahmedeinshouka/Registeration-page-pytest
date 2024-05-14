import unittest
from app import app

class FlaskIntegrationTestCase(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'User Registration', response.data)

    def test_registration(self):
        response = self.app.post('/register', data=dict(
            username='testuser',
            email='test@example.com',
            password='password'
        ), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Registration Successful!', response.data)

        # Verify that the user is added to the database
        # You can add more assertions here to check database state

if __name__ == '__main__':
    unittest.main()
