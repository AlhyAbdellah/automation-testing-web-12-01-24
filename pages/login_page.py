from selenium import webdriver # type: ignore
from selenium.webdriver.common.by import By # type: ignore
from selenium.webdriver.support.ui import WebDriverWait # type: ignore
from selenium.webdriver.support import expected_conditions as EC # type: ignore
from selenium.webdriver.common.action_chains import ActionChains # type: ignore  simulate mouse movements and clicks
import random
import time
from utils.helpers import safe_click_with_cleanup

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(driver)#Use ActionChains to simulate mouse movements and clicks
        self.sign_in_btn = (By.CSS_SELECTOR, "button.signin-header-action")
        self.username_field = (By.ID, "join_neu_email_field")
        self.password_field = (By.ID, "join_neu_password_field")
        self.login_btn = (By.CSS_SELECTOR, '[data-clg-id="WtButton"]')

    def _human_delay(self, min_wait=2, max_wait=6):
        """Random delay between actions to mimic human behavior."""
        time.sleep(random.uniform(min_wait, max_wait)) # Attendre entre 1 et 3 secondes, comme un humain ! 

    def _move_mouse_naturally(self, element):
        """Simulate human-like mouse movement to an element."""
        self.actions.move_to_element(element)
        self.actions.perform()
        self._human_delay()

    def accept_cookies(self):
        """Handle cookie consent banner if present."""
        try:
            cookie_btn = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-gdpr-single-choice-accept='true']"))
            )
            self._move_mouse_naturally(cookie_btn)
            cookie_btn.click()
            self._human_delay()
            print("Cookie consent accepted.")
        except Exception as e:
            print(f"Cookie banner not found or already dismissed: {e}")

    def solve_captcha_manually(self):
        print("🛑 CAPTCHA detected! Solve it manually within 30 seconds...")
        time.sleep(30)  # Pause for manual CAPTCHA solving

    def login(self, username, password):
        self.accept_cookies()

        # Simulate human-like interaction with sign-in button
        sign_in_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.sign_in_btn))
        self._move_mouse_naturally(sign_in_element)
        sign_in_element.click()

        # Randomize typing speed for username/password
        username_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.username_field))
        self._move_mouse_naturally(username_element)
        for char in username:
            username_element.send_keys(char)
            time.sleep(random.uniform(0.1, 0.3))  # Simulate typing speed

        password_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.password_field))
        self._move_mouse_naturally(password_element)
        for char in password:
            password_element.send_keys(char)
            time.sleep(random.uniform(0.1, 0.3))

        # Click login button with natural delay
        login_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.login_btn))
        self._move_mouse_naturally(login_element)
        login_element.click()