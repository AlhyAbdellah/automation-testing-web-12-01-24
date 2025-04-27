from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


# helpers.py (dans ton dossier utils par exemple)

def safe_click(driver, element):
    try:
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        driver.execute_script("arguments[0].click();", element)
        print("✅ Safe click réussi")
    except Exception as e:
        print(f"⚠️ Erreur safe click : {e}")
