
import unittest
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from PageObject.RegistrationPage import RegistrationPage

class TestRegistration(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.RP = RegistrationPage(self.driver)

    def test_registration(self):
        # Load test data from a CSV file
        data = pd.read_csv(r'/home/upaya/Documents/BookCart/TestCase/registration_data.csv')
        
        for index, row in data.iterrows():
            print(row['lastname'])
            self.RP.navigate_to_registration_page()
            self.RP.setFirstName(row['firstname'])
            self.RP.setLastName(row['lastname'])
            self.RP.setUsername(row['username'])
            self.RP.setPassword(row['password'])
            self.RP.setConfirmPassword(row['confirm_password'])
            self.RP.selectGender(row['gender'])
            self.RP.clickRegisterButton()
            
            success_message = self.RP.get_message()

        # Assert for successful registration (based on success message or redirection) currently there is  no sucess message.
        if success_message:
            if "Registration is successful" in success_message:
                self.assertTrue(success_message, f"Registration Sucessful {index}")
            else:
                self.fail(f"No message displayed after registration for row {index}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
