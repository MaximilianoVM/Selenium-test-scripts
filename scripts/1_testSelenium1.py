# selenium 3
from ast import Bytes
from itertools import product
from math import prod
from tkinter import W
from turtle import title
from unicodedata import name
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

#########

from selenium.webdriver.chrome.service import Service as ChromeService

service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

#########

#########driver = webdriver.Chrome(ChromeDriverManager().install())		

#Definir funciones y clases 

#########=================================== CLASES ===================================#########
class Articulo: 

  def __init__(self , nombre , precio): 
    self.nombre = nombre 
    self.precio = precio

#########====================================== METODOS ======================================#########

#######==BURBUJA==#######
def bubbleSortMaMe(listaArticulos): 
  intercambio = True 

  while intercambio: 
    intercambio = False
    for i in range(len(listaArticulos) -1): 
      if(listaArticulos[i].precio < listaArticulos[i+1].precio):
        #intercambiamos los datos
        listaArticulos[i] , listaArticulos[i+1] = listaArticulos[i+1] , listaArticulos[i]
        intercambio = True
  return listaArticulos 

#####==ALMACENAR ELEMENTOS==#####
def almacenarElementos(nombresX , preciosX): 
  #define lista objetos
  listaObjetos = []

  #almacena nombre y precio
  for i in range(len(nombresX)):

    a = Articulo( driver.find_element( By.XPATH , nombresX[i] ).text 
             ,int(driver.find_element( By.XPATH , preciosX[i] ).text.replace(',' , '')  ) ) 
    
    listaObjetos.append(a)
  
  #ordena objetos por precio de mayor a menor
  bubbleSortMaMe(listaObjetos)

  return listaObjetos

#########============================================NAVEGADOR=============================================#########

#ABRIR SITIO
driver.get("https://www.mercadolibre.com.mx/")
driver.implicitly_wait(2)

#OBTENER ARCHIVO TXT
f = open('C:/Users/UABC Becario/Documents/SELENIUM/txt/mercadoLibre.txt')

#REALIZAR BUSQUEDA
driver.find_element(By.XPATH , "/html/body/header/div/form/input" ).send_keys(f.read(9))
driver.implicitly_wait(2)

f.close()

driver.find_element(By.XPATH , "/html/body/header/div/form/button").click()
driver.implicitly_wait(3)

#APLICAR FILTROS

 #nuevo
print("filtro 0")

element = driver.find_element(By.XPATH , '//*[@id="root-app"]/div/div[2]/aside/section/div[7]/ul/li[1]/a/span[1]')

driver.execute_script("arguments[0].click();", element)
driver.implicitly_wait(3)
print("filtro 1")

 #envio gratis
element2 = driver.find_element(By.XPATH , '//*[@id="root-app"]/div/div[2]/aside/section[2]/div[5]/ul/li/a/span[1]')
driver.execute_script("arguments[0].click();", element2)
driver.implicitly_wait(3)
print("filtro 2")


#########======================================INFO PRODUCTOS A TXT=============================================#########
nombresX = []
preciosX = []

for p in 1,2,3,4,5: 
  nombresX.append('//*[@id="root-app"]/div/div[2]/section/ol/li['+str(p)+']//h2')
  preciosX.append('//*[@id="root-app"]/div/div[2]/section/ol/li['+str(p)+']//span[2]/span[2]')

#ENVIAR LISTAS A FUNCION PARA HACER OBJETOS 

listProductos = almacenarElementos(nombresX, preciosX)

#ESCRIBIMOS LISTA EN DOC TXT
f = open('C:/Users/UABC Becario/Documents/SELENIUM/txt/mercadoLibreRes.txt' , 'w')

listaArticulosText = []
for i in range(len(listProductos)): 
    linea = listProductos[i].nombre + ";  $ " + str(listProductos[i].precio) + "\n"
    listaArticulosText.append(linea)

print("==========CONTENIDO DE AAA==========")
for j in range(len(listaArticulosText)): 
  print(listaArticulosText[j])

f.writelines( listaArticulosText )

f.close()
#again open the file for read
f = open('C:/Users/UABC Becario/Documents/SELENIUM/txt/mercadoLibreRes.txt' , 'r')
#reads the file content and prints in console
print("==========CONTENIDO EN EL DOC TXT==========")
print(f.read())
