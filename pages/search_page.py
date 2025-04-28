from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.helpers import safe_click_with_cleanup

class EtsyPage:
    def __init__(self, driver):
        self.driver = driver
        # Locators
        self.search_box = (By.ID, "global-enhancements-search-query")
        self.search_button = (By.CSS_SELECTOR, "button[aria-label='Search']")
        self.results = (By.CLASS_NAME, "v2-listing-card__info")

    def search_product(self, product_name):
        # Enter product name and click search
        self.driver.find_element(*self.search_box).send_keys(product_name)
        self.driver.find_element(*self.search_button).click()
        # Wait for results to load
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.results)
        )

    def close_cookies_banner(self):
        # Close Etsy's GDPR/cookies banner (if present)
        try:
            accept_button = self.driver.find_element(
                By.CSS_SELECTOR, "button[data-gdpr-single-choice-accept='true']"
            )
            accept_button.click()
        except:
            pass  # Banner not present