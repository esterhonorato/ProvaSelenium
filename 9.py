from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import time
from selenium.webdriver.common.keys import Keys

navegador = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install())) 
navegador.get("https://www.kabum.com.br/")
time.sleep(3)
#fechar cookie 
navegador.find_element(By.XPATH, '/html/body/div[7]/div[2]/div/div/div[2]/div/div').click()
time.sleep(2)

navegador.quit()
