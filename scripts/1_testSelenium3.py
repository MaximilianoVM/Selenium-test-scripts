# selenium 3
from ast import Bytes
from datetime import date, datetime
from itertools import product
from math import prod
from select import select
from sqlite3 import Date
from tkinter import W, Image
from turtle import title
from unicodedata import name
from xml.dom.minidom import Element
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

import time

driver = webdriver.Chrome(ChromeDriverManager().install())	

#########====================================== NAVEGADOR ======================================#########

#ABRIR SITIO
driver.get("https://www.mercadolibre.com.mx/")
driver.implicitly_wait(2)

#REALIZAR BUSQUEDA
driver.find_element(By.XPATH , "/html/body/header/div/form/input" ).send_keys("uno cartas")
driver.implicitly_wait(2)
driver.find_element(By.XPATH , "/html/body/header/div/form/button").click()
driver.implicitly_wait(2)

time.sleep(2)

#guardamos los datos de la fecha actual como atributos de un objeto currentTime
currentTime = datetime.now()

#seleccionar el primer elemento 
driver.find_element(By.XPATH , '//*[@id="root-app"]/div/div[2]/section/ol/li[1]//h2').click()
time.sleep(7)

dateNow = datetime.now()
dateNowStr = str(dateNow)

driver.save_screenshot( dateNowStr + '.png' )
driver.implicitly_wait(2)
time.sleep(7)


