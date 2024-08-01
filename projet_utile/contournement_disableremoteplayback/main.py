from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Chemin vers ton WebDriver
webdriver_path = ('C:/Users/jefou/OneDrive/Documents/PycharmProjects/Hello_world/projet_utile/'
                  'contournement_disableremoteplayback/chrome_driver/chromedriver.exe')

# Initialiser le WebDriver
driver = webdriver.Chrome(webdriver.Chrome(webdriver_path))

# Ouvrir la page web
url = ('https://thetvapp.to/tv/cartoon-network-live-stream/?fbclid=IwZXh0bgNhZW0CMTEAAR32pO2H1fIYVNdzLIDssdnrpczwr'
       '5LeMBhLsxUf4JzojC0Rov7T5H-Q1Ys_aem_IF4GbKFhnCpvK-kcqi4mVw')  # Change cette URL
driver.get(url)

# Attendre que la page se charge
time.sleep(5)

# Trouver l'élément <video> et supprimer l'attribut 'disableremoteplayback'
video_element = driver.find_element(By.TAG_NAME, 'video')
driver.execute_script("arguments[0].removeAttribute('disableremoteplayback')", video_element)

# Vérifier que l'attribut a été supprimé
print(video_element.get_attribute('disableremoteplayback'))  # Devrait imprimer 'None'

# Fermer le navigateur
driver.quit()
