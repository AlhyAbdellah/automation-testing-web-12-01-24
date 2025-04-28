# pages/logged_in_delete_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.helpers import safe_click_with_cleanup

class LoggedInDeletePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Locators
    logged_in_as_text = (By.XPATH, "//a[contains(text(),'Logged in as')]")
    delete_account_link = (By.LINK_TEXT, "Delete Account")
    account_deleted_text = (By.XPATH, "//b[text()='Account Deleted!']")
    continue_button_after_delete = (By.XPATH, "//a[@data-qa='continue-button']")

    # Actions
    def is_logged_in_as_visible(self):
        return self.wait.until(EC.visibility_of_element_located(self.logged_in_as_text))

    def click_delete_account(self):
        
        safe_click_with_cleanup(self.driver, self.delete_account_link)

    def is_account_deleted_visible(self):
        return self.wait.until(EC.visibility_of_element_located(self.account_deleted_text))

    def click_continue_after_delete(self):
        
        safe_click_with_cleanup(self.driver, self.continue_button_after_delete)
