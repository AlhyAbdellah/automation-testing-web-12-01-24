from appium import webdriver
from time import sleep

# Paramètres de configuration
desired_caps = {
    'platformName': 'Android', 
    'platformVersion': '13', 
    'deviceName': 'R9YT911GDGR', 
    'appPackage': 'com.whatsapp.w4b',
    'appActivity': 'com.whatsapp.w4b.HomeActivity',
    'noReset': True,
    'automationName': 'UiAutomator2'  # Ajouter cette ligne pour préciser l'automatisation
}


# Création de la session Appium
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

def unlock_phone(pin_code):
    """
    Fonction pour déverrouiller le téléphone avec un code PIN.
    """
    for digit in pin_code:
        driver.press_keycode(int(digit))  # Simule la touche correspondant au chiffre
        sleep(0.5)

# Déverrouiller le téléphone avant de lancer WhatsApp
unlock_phone("199898a")

# Attendre un peu pour s'assurer que le téléphone est déverrouillé
sleep(3)

# Vérification de l'écran d'accueil de WhatsApp (exemple d'interaction)
try:
    # Ici, nous vérifions si l'élément d'accueil est visible (exemple : l'élément du bouton 'Nouveau message')
    home_button = driver.find_element_by_accessibility_id('Nouveau message')
    if home_button.is_displayed():
        print("Test Réussi : Bouton 'Nouveau message' trouvé sur l'écran d'accueil.")
    else:
        print("Échec : Le bouton 'Nouveau message' n'est pas visible.")

    # Cliquer sur le bouton 'Nouveau message' (pour tester l'interaction)
    home_button.click()

    # Attendre quelques secondes pour s'assurer que la liste des contacts est chargée
    sleep(2)

    # Rechercher et cliquer sur le contact "Btissam"
    contact_name = "Btissam"  # Le nom de votre femme dans les contacts WhatsApp
    contact = driver.find_element_by_xpath(f"//android.widget.TextView[@text='{contact_name}']")
    contact.click()

    # Attendre quelques secondes pour s'assurer que la conversation se charge
    sleep(2)

    # Trouver le champ de texte pour envoyer un message
    message_field = driver.find_element_by_id('com.whatsapp:id/entry')
    message_field.click()

    # Saisir un message dans le champ de texte
    message = "Salut Btissam, je t'aime !"
    message_field.send_keys(message)

    # Trouver et cliquer sur le bouton d'envoi du message
    send_button = driver.find_element_by_id('com.whatsapp:id/send')
    send_button.click()

    print(f"Test Réussi : Message '{message}' envoyé à Btissam.")

except Exception as e:
    print(f"Erreur lors du test : {e}")

# Fermer l'application après le test
driver.quit()