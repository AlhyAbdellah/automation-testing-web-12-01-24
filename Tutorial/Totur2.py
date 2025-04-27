from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdrievr.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time 
import random

url = "https://www.linkedin.com/feed/"

driver = webdriver.Chrome()

driver.get(url)
time.sleep(10)

Username = WebDriverWait (driver,5).until(EC.visibility_of_element_located.by(By.ID""))
username.send_keys("")
username.click()
driver.quit()