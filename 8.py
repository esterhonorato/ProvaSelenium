from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import time
from selenium.webdriver.common.keys import Keys

navegador = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install())) 
navegador.get("https://www.selenium.dev/")
time.sleep(5)

try:
    navegador.find_element(By.LINK_TEXT, "Downloads").click()
    time.sleep(3)

    # Extrair o texto do cabeçalho principal
    header = navegador.find_element(By.TAG_NAME, "h2")
    print("Texto do cabeçalho:", header.text)

finally:
    navegador.quit()