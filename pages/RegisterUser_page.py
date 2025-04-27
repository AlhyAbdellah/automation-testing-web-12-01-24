from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import random
import time 

# 🔧 Fonctions utilitaires robustes
def safe_click(element):
    try:
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        driver.execute_script("arguments[0].click();", element)
        print("✅ Safe click réussi")
    except Exception as e:
        print(f"⚠️ Erreur lors du safe click : {e}")

def safe_send_keys(element, text):
    try:
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.clear()
        element.send_keys(text)
        print(f"✅ Texte envoyé : {text}")
    except Exception as e:
        print(f"⚠️ Erreur lors de l’envoi du texte : {e}")

#Initialisation
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://automationexercise.com")
wait = WebDriverWait(driver, 10)

# Attente de la page d'accueil
wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@alt='Website for automation practice']")))
print("Home page visible")

# Popup
try:
    close_ad_btn = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@id='dismiss-button']//span"))
    )
    close_ad_btn.click()
    print("✅ Popup détecté et fermé")
except:
    print("✅ Aucun popup détecté, on continue")

# Cliquer sur "Signup / Login"
wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Signup / Login"))).click()
print("Signup / Login clicked")

# Vérifier "New User Signup!"
wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='New User Signup!']")))
print("New User is visible")

# Entrer nom + email
name = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@data-qa='signup-name']")))
email = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@data-qa='signup-email']")))

fake_email = f"test{random.randint(1000,9999)}@gmail.com"
safe_send_keys(name, "alhy")
safe_send_keys(email, fake_email)
print(f"nom et email saisis : {fake_email}")

# Cliquer sur "Signup" (changement de page donc clic normal)
wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-qa='signup-button']"))).click()
print("Signup clicked")

# Vérifier "Enter Account Information"
wait.until(EC.visibility_of_element_located((By.XPATH, "//b[text()='Enter Account Information']")))
print("ACCOUNT INFO IS VISIBLE")

# Remplir les infos
safe_click(driver.find_element(By.ID, "id_gender1"))
safe_send_keys(driver.find_element(By.ID, "password"), "tes123@")

day = driver.find_element(By.ID, "days")
d=random.randint(1,31)
Select (day).select_by_index(d)
print (f"Day is {d}")

Month = driver.find_element(By.ID, "months")
m=random.randint(1,12)
Select (Month).select_by_index(m)
print(f"Month is {m}")

year = driver.find_element(By.ID, "years")
y=random.randint(1,100)
Select(year).select_by_index(y)
print(f"Year is {y}")

print("infos remplies")

# Cases à cocher
safe_click(driver.find_element(By.ID, "newsletter"))
safe_click(driver.find_element(By.ID, "optin"))

# Fonction raccourcie pour trouver un élément
def find(by, selector):
    return driver.find_element(by, selector)

# Remplir les infos d'adresse
safe_send_keys(find(By.ID, "first_name"), "tester")
safe_send_keys(find(By.ID, "last_name"), "QA")
safe_send_keys(find(By.ID, "company"), "TechQA")
safe_send_keys(find(By.ID, "address1"), "1 rue de l'horloge")

contry = find(By.ID, "country")
c=random.randint(1,4)
Select(contry).select_by_index(c)
print(f"Contry is {c}")

safe_send_keys(find(By.ID, "state"), "Québec")
safe_send_keys(find(By.ID, "city"), "Montréal")
safe_send_keys(find(By.ID, "zipcode"), "H2X1Y4")
safe_send_keys(find(By.ID, "mobile_number"), "0612345678")
print("✅ Infos d'adresse remplies")

# Créer le compte (changement de page donc clic normal)
wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-qa='create-account']"))).click()
print("Create Account clicked")

# Vérifier "Account Created"
wait.until(EC.visibility_of_element_located((By.XPATH, "//b[text()='Account Created!']")))

# Cliquer sur "Continue" (changement de page donc clic normal)
wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@data-qa='continue-button']"))).click()
print("Continue clicked")

# Vérifier "Logged in as"
wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Logged in as')]")))
print("Logged in as visible")

# Supprimer le compte (changement de page donc clic normal)
wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Delete Account"))).click()
print("Delete Account clicked")

# Vérifier suppression
wait.until(EC.visibility_of_element_located((By.XPATH, "//b[text()='Account Deleted!']")))
print("ACCOUNT DELETED")

# Fin (continue après delete)
wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@data-qa='continue-button']"))).click()
print("End of Script")
print("Alhamdoli ALLAH")

driver.quit()
