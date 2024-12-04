from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import time
from selenium.webdriver.common.keys import Keys

navegador = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install())) 
navegador.get("https://www.google.com.br/")
time.sleep(5)

search_bar = navegador.find_element("name", "q")
search_bar.send_keys("Python Selenium")
search_bar.send_keys(Keys.RETURN)
time.sleep(5)

navegador.save_screenshot("resultado.png")
navegador.quit()