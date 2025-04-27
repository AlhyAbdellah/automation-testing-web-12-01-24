from selenium import webdriver # type: ignore
from selenium.webdriver.chrome.options import Options # type: ignore
from selenium.webdriver.support.ui import WebDriverWait  # type: ignore # Added import
from selenium.webdriver.support import expected_conditions as EC  # Added import
from pages.login_page import LoginPage

def setup_browser():
    options = Options()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--start-maximized")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    driver = webdriver.Chrome(options=options)
    return driver

def test_login():
    driver = setup_browser()
    driver.get("https://www.etsy.com/")
    
    login_page = LoginPage(driver)
    login_page.login("alhy.abdellah@gmail.com", "Lwalida1998@")
    
    # Post-login validation
    WebDriverWait(driver, 15).until(
        EC.url_contains("etsy.com/you")  # Wait for account page
    )
    
    driver.quit()