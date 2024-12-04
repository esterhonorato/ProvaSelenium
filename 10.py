from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import time
from selenium.webdriver.common.keys import Keys

navegador = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install())) 
navegador.get("https://the-internet.herokuapp.com/login")
time.sleep(3)

try:
    navegador.find_element(By.XPATH, '//*[@id="username"]').send_keys("tomsmith")
    time.sleep(3)
    navegador.find_element(By.XPATH, '//*[@id="password"]').send_keys("SuperSecretPassword!")
    time.sleep(3)
    navegador.find_element(By.XPATH, '/html/body/div[2]/div/div/form/button').click()
    time.sleep(3)

    validar = navegador.find_element(By.ID, "flash").text
    if "You logged into a secure area!" in validar:
        print("Login bem-sucedido")
    else:
        print("Erro no login")
finally:
    navegador.quit()