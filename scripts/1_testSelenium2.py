# selenium 3
from ast import Bytes
from itertools import product
from math import prod
from select import select
from tkinter import W
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

#########

from selenium.webdriver.chrome.service import Service as ChromeService

service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

#########

#########driver = webdriver.Chrome(ChromeDriverManager().install())	


elementos = []
#########====================================== METODOS ======================================#########

def tomarElementos(xElementos): 
    element = driver.find_element(By.XPATH , xElementos).text
    elementos.append(element)
    return elementos

	
#########====================================== NAVEGADOR ======================================#########

#ABRIR SITIO
driver.get("https://www.amazon.com.mx")
driver.implicitly_wait(2)
time.sleep(5)

#SELECCIONAR DROPDOWN
dropdown = driver.find_element(By.ID, "searchDropdownBox")
dd = Select(dropdown)

#DEFINIMOS UNA LISTA QUE CONTENGA CADA UNA DE LAS OPCIONES EN FORMATO DE TEXTO
listOptionsText = []

#ALMACENAMOS/IMPRIMIMOS EL TEXTO DE CADA UNO DE LOS ELEMENTOS EN LA LISTA DEFINIDA ANTERIORMENTE
contador = 0
for i in (dd.options): 
    print(i.text)
    contador += 1
    if contador >1 and contador <28 or contador >32: 
        #28 ya no a 32 tampoco
        listOptionsText.append(i.text + " \n")
print("el numero de elementos es: " + str(contador-6) + ", sin incluir 'Todas las categorías', 'Mujeres', 'Hombres, 'Ninas' , 'Ninos', 'Bebe' ")

time.sleep(3)

#########====================================== DOCUMENTO ======================================#########

#ESCRIBIMOS CADA UNO DE LOS ELEMENTOS EN UN ARCHIVO TXT
f = open( 'C:/Users/UABC Becario/Documents/SELENIUM/txt/amazonOpciones.txt' , 'w')

f.writelines( listOptionsText )

f.close()
#again open the file for read
f = open('C:/Users/UABC Becario/Documents/SELENIUM/txt/amazonOpciones.txt' , 'r')

#reads the file content and prints in console
print("==============CONTENIDO EN EL DOC TXT==============")
print(f.read())

#########====================================== BUSQUEDA ======================================#########
########## "LEER LAS OPCIONES DESDE EL ARCHIVO Y BUSCARLAS EN GOOGLE" ##########

#ABRIR NUEVA VENTANA 

for p in range(len(listOptionsText)): 
    driver.execute_script("window.open('');")

    driver.implicitly_wait(2)
    time.sleep(2)

    driver.switch_to.window(driver.window_handles[p])
    #ABRIR SITIO
    driver.get('https://www.google.com')
    productoBuscar = listOptionsText[p]
    driver.implicitly_wait(2)
    time.sleep(2)
    driver.find_element(By.XPATH , "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input").send_keys(productoBuscar)


time.sleep(70)

driver.close
