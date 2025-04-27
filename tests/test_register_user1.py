# tests/test_register_user.py

import pytest
from selenium import webdriver
import random
from pages.home_page import HomePage
from pages.signup_page import SignupPage
from pages.account_info_page import AccountInfoPage
from pages.account_created_page import AccountCreated
from pages.logged_in_delete_page import LoggedInDeletePage
from utils.data_loader import user_file_excel

user_data = user_file_excel("../data/users.xlsx")

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://automationexercise.com")
    yield driver
    driver.quit()
print("hello")
@pytest.mark.parametrize(
    "name, password, day, month, year, first_name, last_name, company, address1, country, state, city, zipcode, mobile",
    user_data)
def test_register_user_data_driven(setup, name, password, day, month, year, first_name, last_name, company, address1, country, state, city, zipcode, mobile):
    driver = setup

    # Instancier les pages
    home_page = HomePage(driver)
    signup_page = SignupPage(driver)
    account_info_page = AccountInfoPage(driver)
    account_created_page = AccountCreated(driver)
    logged_in_delete_page = LoggedInDeletePage(driver)

    # Étapes du test
    home_page.popup()
    home_page.click_signup()

    assert signup_page.new_user_visible()
    fake_email = f"test{random.randint(1000,9999)}@gmail.com"
    signup_page.fill_name_email("alhy", fake_email)
    signup_page.click_signup_button()

    assert account_info_page.is_enter_account_info_visible()
    account_info_page.fill_all_form(
        password=password,
        day=str(day),
        month=month,
        year=str(year),
        first_name=first_name,
        last_name=last_name,
        company=company,
        address1=address1,
        country=country,
        state=state,
        city=city,
        zipcode=str(zipcode),
        mobile=str(mobile)
    )
    account_info_page.click_create_account()

    assert account_created_page.Account_visibl()
    account_created_page.click_continue()

    assert logged_in_delete_page.is_logged_in_as_visible()
    logged_in_delete_page.click_delete_account()
    assert logged_in_delete_page.is_account_deleted_visible()
    logged_in_delete_page.click_continue_after_delete()
    print("CI/CD Pipline work fine")
    print("alhamdoli Allah")
