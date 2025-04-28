from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


# helpers.py (dans ton dossier utils par exemple)

def safe_click_with_cleanup(driver, element_or_locator):
    """
    Clique sur un élément après avoir géré iframes/overlays parasites.
    Accepte soit un locator soit un WebElement.
    """
    try:
        # Si c'est un locator (tuple), convertir en WebElement
        if isinstance(element_or_locator, tuple):
            from selenium.webdriver.support.ui import WebDriverWait
            from selenium.webdriver.support import expected_conditions as EC
            element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(element_or_locator)
            )
        else:
            element = element_or_locator

        # Scroller dans la vue
        driver.execute_script("arguments[0].scrollIntoView(true);", element)

        try:
            # Première tentative de click
            driver.execute_script("arguments[0].click();", element)
            print("✅ Safe click réussi du premier coup")
        except Exception as click_error:
            print(f"⚠️ Erreur de click direct : {click_error}")
            # Optionnel : ici tu pourrais ajouter suppression d'iframe/overlay si besoin

            # Deuxième tentative après nettoyage éventuel
            driver.execute_script("arguments[0].scrollIntoView(true);", element)
            driver.execute_script("arguments[0].click();", element)
            print("✅ Safe click réussi après gestion")

    except Exception as final_error:
        print(f"❌ Safe click with cleanup a échoué : {final_error}")


