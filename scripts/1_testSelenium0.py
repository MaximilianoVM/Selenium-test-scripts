# selenium 3
from ast import Bytes
from turtle import title
from unicodedata import name
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import time


driver = webdriver.Chrome(ChromeDriverManager().install())		
        
#ABRIR INDEX
driver.get("https://www.amazon.com.mx/")
#time.sleep(2)
#driver.maximize_window()
time.sleep(2)
		
#BUSCAR PRODUCTO
driver.find_element(By.XPATH , "//*[@id=\"twotabsearchtextbox\"]" ).send_keys("audifonos")
time.sleep(2)
driver.find_element(By.XPATH , " /html/body/div[1]/header/div/div[1]/div[2]/div/form/div[4]/div/span/input ").click()
time.sleep(2)

#SELECCIONAR PRODUCTO
driver.implicitly_wait(2)
driver.find_element(By.XPATH , "/html/body/div[1]/div[2]/div[1]/div[1]/div/span[3]/div[2]/div[3]/div/div/div/div/div/div/div[1]/span/a/div" ).click()
time.sleep(2)
		
#AÑADIR AL CARRITO
driver.implicitly_wait(2)
driver.find_element(By.XPATH , " /html/body/div[4]/div[3]/div[4]/div[11]/div[1]/div[5]/div/div/div/div/form/div/div/div/div/div[3]/div/div[13]/div[1]/span/span/span/input " ).click()
time.sleep(2)

#CERRAR PESTAÑA
driver.implicitly_wait(10)
time.sleep(10)
driver.close()
