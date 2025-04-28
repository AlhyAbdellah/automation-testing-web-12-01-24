# pages/signup_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.helpers import safe_click_with_cleanup

class SignupPage:

    def __init__(self, driver):  # ATTENTION ici : c'est __init__ (avec double underscore) !
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Locators
    name_field = (By.XPATH, "//input[@data-qa='signup-name']")
    email_field = (By.XPATH, "//input[@data-qa='signup-email']")
    signup_button = (By.XPATH, "//button[@data-qa='signup-button']")
    new_user_text = (By.XPATH, "//h2[text()='New User Signup!']")

    # Actions
    def new_user_visible(self):
        return self.wait.until(EC.visibility_of_element_located(self.new_user_text))
    
    def fill_name_email(self, name, email):
        self.wait.until(EC.presence_of_element_located(self.name_field)).send_keys(name)
        self.wait.until(EC.presence_of_element_located(self.email_field)).send_keys(email)
    
    def click_signup_button(self):
        safe_click_with_cleanup(self.driver, self.signup_button)
