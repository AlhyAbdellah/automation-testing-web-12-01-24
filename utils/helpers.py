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

def safe_click_with_cleanup(driver, element_or_locator):
    try:
        # Vérifier si c'est un locator (tuple) et pas déjà un WebElement
        if isinstance(element_or_locator, tuple):
            element = driver.find_element(*element_or_locator)
        else:
            element = element_or_locator

        # Scroller dans la vue
        driver.execute_script("arguments[0].scrollIntoView(true);", element)

        # Essayer de cliquer
        driver.execute_script("arguments[0].click();", element)
        print("✅ Safe click réussi")
    except Exception as e:
        print(f"⚠️ Erreur safe click with cleanup: {e}")

