from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    
    def __init__(self,driver):
        self.driver=driver
        self.wait= WebDriverWait(driver,10)

    #locator pour bouton singup / Login
    signup_login = (By.LINK_TEXT,"Signup / Login")
    consent_data = (By.XPATH, "//button[contains(@class,'fc-primary-button')]")


    #pop up Consent Data
    def popup(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.consent_data)).click()
            print("pop up passé")
        except Exception as e :
            print("pas de pop up")

    #Méthode pour cliquer bouton
    def click_signup(self):
        self.wait.until(EC.element_to_be_clickable(self.signup_login)).click()
        print("Signup cliqué depuis page Home")