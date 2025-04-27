# conftest.py (dans ton projet racine)

import pytest
import os

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # 1. Cette fonction est appelée à chaque fin de test (passé ou échoué)
    
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        # 2. Si le test échoue à l'étape principale ("call")
        
        driver = item.funcargs.get("setup")
        # 3. Récupérer l'objet WebDriver utilisé par le test
        
        if driver:
            # 4. S'il y a bien un driver actif

            # Créer dossier screenshots s'il existe pas
            if not os.path.exists("screenshots"):
                os.makedirs("screenshots")

            screenshot_name = f"screenshots/{item.name}.png"
            driver.save_screenshot(screenshot_name)
            print(f"📸 Screenshot sauvegardé : {screenshot_name}")
