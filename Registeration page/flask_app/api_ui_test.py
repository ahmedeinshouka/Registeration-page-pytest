import unittest
from selenium import webdriver

class APIUITestCase(unittest.TestCase):
    def setUp(self):
        
        self.driver = webdriver.Chrome()
        self.base_url = 'http://localhost:5000'  

    def tearDown(self):
        # Close the WebDriver session
        self.driver.quit()

    def test_registration_page(self):
        # Test registration page UI
        self.driver.get(f'{self.base_url}/')
        self.assertIn('User Registration', self.driver.title)

        
        username_input = self.driver.find_element_by_id('username')
        email_input = self.driver.find_element_by_id('email')
        password_input = self.driver.find_element_by_id('password')
        register_button = self.driver.find_element_by_xpath('//button[contains(text(), "Register")]')

        
        username_input.send_keys('testuser')
        email_input.send_keys('test@example.com')
        password_input.send_keys('password')

        # Submit registration form
        register_button.click()

        # Assert registration success message
        success_message = self.driver.find_element_by_xpath('//div[contains(text(), "Registration Successful!")]')
        self.assertTrue(success_message.is_displayed())

if __name__ == '__main__':
    unittest.main()
