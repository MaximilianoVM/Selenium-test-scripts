#########========

from imports import *
#from clases import Articulo
from metodos import *

#########========

import time

#########

from selenium.webdriver.chrome.service import Service as ChromeService

service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

#########====================================== METODOS ======================================#########

def busquedaML(busqueda): 
    driver.find_element(By.XPATH , "/html/body/header/div/form/input" ).send_keys(busqueda)
    driver.implicitly_wait(2)

    driver.find_element(By.XPATH , "/html/body/header/div/form/button").click()
    driver.implicitly_wait(3)

def filtroMinMax(min,max): 

    element = driver.find_element(By.XPATH , '//*[@id="root-app"]/div/div[2]/aside/section//ul/li[4]/form/div[1]/div/label/div/input')

    #minimo
    element.send_keys(str(min))
    driver.implicitly_wait(3)
    print("MINIMO INGRESADO")

    #maximo
    element2 = driver.find_element(By.XPATH , '//*[@id="root-app"]/div/div[2]/aside/section//ul/li[4]/form/div[2]/div/label/div/input')
    element2.send_keys(str(max))
    driver.implicitly_wait(3)
    print("MAXIMO INGRESADO")

    #aplicar
    element3 = driver.find_element(By.XPATH , '/html/body/main/div/div[2]/aside/section//ul/li[4]/form/div[3]/button')
    driver.execute_script("arguments[0].click();", element3)
    driver.implicitly_wait(3)
    print("FILTROS APLICADOS")

#########============================================NAVEGADOR=============================================#########

#ABRIR SITIO
driver.get("https://www.mercadolibre.com.mx/")
driver.implicitly_wait(2)

#REALIZAR BUSQUEDA

busquedaML('reloj casio')

#APLICAR FILTROS (Filtrar la búsqueda por precio 300 a 3000)
print("FILTROS")
filtroMinMax(300,3000)

time.sleep(3)
driver.implicitly_wait(3)

time.sleep(2)

#########======================================INFO PRODUCTOS A TXT=============================================#########
nombresX = []
preciosX = []
estrellasX =  []
recomendacionesX =  []

print("==============================CICLO INICIADO==============================")

for p in 1,2,3,4,5: 
  print("---------------- CICLO "+str(p)+" ----------------")
  time.sleep(2)

  #obtiene el link para la pagina del articulo
  time.sleep(2)
  if(p%2 == 0):
    secProducto = driver.find_element(By.XPATH, '//*[@id="root-app"]/div/div[2]/section/ol['+str(p-1)+']/li['+str(2)+']/div/div/a')

  else:
    if p==1:
      p=2
      m=2 #En cualquier otro caso, m=0

    secProducto = driver.find_element(By.XPATH, '//*[@id="root-app"]/div/div[2]/section/ol['+str(p-1)+']/li['+str(1)+']/div/div/a')

    if m==2: p=1

  time.sleep(2)
  linkProducto = secProducto.get_attribute("href")
            
  #abre una nueva ventana
  driver.execute_script("window.open('');")
  driver.implicitly_wait(2)
  time.sleep(2)

  #cambia a la ventana nueva
  driver.switch_to.window(driver.window_handles[p])   

  #ingresa al link del articulo obtenido anteriormente
  driver.get(linkProducto)

  #obtiene el link de la pagina de reseñas para el articulo
  time.sleep(5)

  #almacena nombres y precios en listas
  nombresX.append( driver.find_element( By.XPATH , '//*[@id="header"]/div/div[2]/h1' ).text )
  print( "Descripcion: " + nombresX[p-1] )
  preciosX.append(driver.find_element( By.XPATH , '//*[@id="price"]/div/div[1]//span[3]' ).text)  
  print( "Precio: $" + preciosX[p-1] )

  #el "if" confirma que el producto tenga estrellas
  if driver.find_elements(By.CSS_SELECTOR, '#header > div > div.ui-pdp-header__info > a'): 
      secEstrellas = driver.find_element(By.CSS_SELECTOR, '#header > div > div.ui-pdp-header__info > a')
      time.sleep(3)
      linkEstrellas = secEstrellas.get_attribute("href")

      #ingresa al link de la pagina de reseñas
      time.sleep(3)
      driver.get(str(linkEstrellas))

      #obtiene la cantidad de estrellas y la almacena en una lista
      time.sleep(3)
      thisEstrellas = str(driver.find_element(By.XPATH, '//*[@id="reviews-capability.desktop"]/section/div[2]/div[1]/article/div/div[1]/div[1]/p').text)
      print("$$$$$$ THIS ESTRELLAS: " + str(thisEstrellas))
      estrellasX.append(str(thisEstrellas))

  else: 
      estrellasX.append("Este producto aun no tiene reseñas")
      print("Este producto aun no tiene reseñas")

  #regresa a la ventana original
  driver.switch_to.window( driver.window_handles[0] )

  m=1
  print(" CICLO "+str(p)+" TERMINADO ")
print("==============================CICLO TERMINADO==============================")

#ENVIAR LISTAS A FUNCION PARA HACER OBJETOS 

listProductos = almacenarElementos(nombresX, preciosX, estrellasX)

listaArticulosText = []
for i in range(len(listProductos)): 
    linea = listProductos[i].nombre + "\n" +"   $ " + str(listProductos[i].precio) + "\n" + "   Estrellas:" + str(listProductos[i].estrellas) +"\n" + "   Recomendacion:" + str(listProductos[i].recomendacion) +"\n" 
    listaArticulosText.append(linea)

print("==========CONTENIDO DE LA LISTA DE ARTICULOS==========")
for j in range(len(listaArticulosText)): 
  print(listaArticulosText[j])
  

driver.close()