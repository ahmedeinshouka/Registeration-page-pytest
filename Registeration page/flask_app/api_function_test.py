import unittest
import requests

class APIFunctionTestCase(unittest.TestCase):
    def setUp(self):
        self.base_url = 'http://localhost:5000'  

    def test_registration(self):
        
        data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'password'
        }
        response = requests.post(f'{self.base_url}/register', data=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Registration Successful!', response.text)

        

    
       

if __name__ == '__main__':
    unittest.main()
