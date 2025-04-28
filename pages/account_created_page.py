from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.helpers import safe_click_with_cleanup

class AccountCreated:

    def __init__(self,driver):
        self.driver = driver
        self.wait =WebDriverWait(driver,10)


 # Locators
    account_created_text = (By.XPATH, "//b[text()='Account Created!']")
    continue_button = (By.XPATH, "//a[@data-qa='continue-button']")

    def     Account_visibl(self):
        return self.wait.until(EC.visibility_of_element_located(self.account_created_text))

    def click_continue(self):
        safe_click_with_cleanup(self.driver, self.continue_button)