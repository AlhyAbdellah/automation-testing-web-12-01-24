# pages/account_info_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from utils.helpers import safe_click

class AccountInfoPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Locators
    enter_account_info_text = (By.XPATH, "//b[text()='Enter Account Information']")
    title_mr = (By.ID, "id_gender1")
    password_field = (By.ID, "password")
    days_dropdown = (By.ID, "days")
    months_dropdown = (By.ID, "months")
    years_dropdown = (By.ID, "years")
    newsletter_checkbox = (By.ID, "newsletter")
    offers_checkbox = (By.ID, "optin")
    first_name_field = (By.ID, "first_name")
    last_name_field = (By.ID, "last_name")
    company_field = (By.ID, "company")
    address1_field = (By.ID, "address1")
    country_dropdown = (By.ID, "country")
    state_field = (By.ID, "state")
    city_field = (By.ID, "city")
    zipcode_field = (By.ID, "zipcode")
    mobile_field = (By.ID, "mobile_number")
    create_account_button = (By.XPATH, "//button[@data-qa='create-account']")

    # Actions
    def is_enter_account_info_visible(self):
        return self.wait.until(EC.visibility_of_element_located(self.enter_account_info_text))

    def fill_all_form(self, password, day, month, year, first_name, last_name, company, address1, country, state, city, zipcode, mobile):
        # Remplir les informations de compte
        self.wait.until(EC.element_to_be_clickable(self.title_mr)).click()
        self.wait.until(EC.visibility_of_element_located(self.password_field)).send_keys(password)
        Select(self.driver.find_element(*self.days_dropdown)).select_by_visible_text(str(day))
        Select(self.driver.find_element(*self.months_dropdown)).select_by_visible_text(month)
        Select(self.driver.find_element(*self.years_dropdown)).select_by_visible_text(str(year))

        # Cochez les cases newsletter et offers
        safe_click(self.driver, self.driver.find_element(*self.newsletter_checkbox))
        self.wait.until(EC.element_to_be_clickable(self.offers_checkbox)).click()

        # Remplir l'adresse
        self.wait.until(EC.visibility_of_element_located(self.first_name_field)).send_keys(first_name)
        self.driver.find_element(*self.last_name_field).send_keys(last_name)
        self.driver.find_element(*self.company_field).send_keys(company)
        self.driver.find_element(*self.address1_field).send_keys(address1)
        Select(self.driver.find_element(*self.country_dropdown)).select_by_visible_text(country)
        self.driver.find_element(*self.state_field).send_keys(state)
        self.driver.find_element(*self.city_field).send_keys(city)
        self.driver.find_element(*self.zipcode_field).send_keys(zipcode)
        self.driver.find_element(*self.mobile_field).send_keys(mobile)

    def click_create_account(self):
        self.wait.until(EC.element_to_be_clickable(self.create_account_button)).click()
