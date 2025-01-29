import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegistrationPage:
    def __init__(self, driver):
        self.driver = driver
        self.baseUrl = "https://bookcart.azurewebsites.net/register"
        self.firstname_xpath = '//input[@placeholder="First name"]'
        self.lastname_xpath = "//mat-form-field//mat-label[normalize-space(text())='Last name']/ancestor::mat-form-field//input"
        self.username_xpath = '//input[@placeholder="User name"]'
        self.password_xpath='//input[@placeholder="Password"]'
        self.confirmpassword_xpath='//input[@placeholder="Confirm Password"]'
        self.gender_male_xpath = "//input[@value='Male']"
        self.gender_female_xpath = "//input[@value='Female']"
        self.register_button_xpath = "//span[normalize-space()='Register']"

    def navigate_to_registration_page(self):
        self.driver.get(self.baseUrl)
        
    def setFirstName(self, firstname):
        firstname_input = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, self.firstname_xpath))
        )
        firstname_input.clear()  # Clears any existing text
        firstname_input.send_keys(firstname)

    def setLastName(self, lastname):
            label = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.lastname_xpath))
        )
            label.click()
            label.clear()  # Clears any existing text
            label.send_keys(lastname)

    def setUsername(self, username):
        username_input = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, self.username_xpath))
        )
        username_input.clear()  # Clears any existing text

        username_input.send_keys(username)

    def setPassword(self, password):
        password_input = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, self.password_xpath))
        )
        password_input.clear()  # Clears any existing text

        password_input.send_keys(password)

    def setConfirmPassword(self, confirm_password):
        confirm_password_input = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, self.confirmpassword_xpath))
        )
        confirm_password_input.clear()  # Clears any existing text

        confirm_password_input.send_keys(confirm_password)
        
    def selectGender(self, gender):
        if gender.lower() == 'male':
            gender_radio = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, self.gender_male_xpath))
            )
        elif gender.lower() == 'female':
            gender_radio = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, self.gender_female_xpath))
            )
        gender_radio.click()

    def clickRegisterButton(self):
        register_button = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.register_button_xpath))
        )
        register_button.click()
        
    def get_message(self):
            try:
                # Wait for the message element to be visible
                message_element = WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located((By.LINK_TEXT, "Login"))  # Replace with the correct ID
                )
                return message_element.text.strip() if message_element else None
            except:
                # If message is not found or another error occurs, return an empty string or a default error message
                return "" 

