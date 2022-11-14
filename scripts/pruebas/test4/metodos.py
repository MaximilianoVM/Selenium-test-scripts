from clases import Articulo

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
def almacenarElementos(nombresX , preciosX, estrellasX): 
  #define lista objetos
  listaObjetos = []

  #almacena nombre y precio
  for i in range(len(nombresX)):

    #a = Articulo( nombresX[i] , int(preciosX[i].text.replace(',' , '')) , estrellasX[i] )  
    a = Articulo( nombresX[i] , int(preciosX[i].replace(',','')) , estrellasX[i] )  
    
    listaObjetos.append(a)
  
  #ordena objetos por precio de mayor a menor
  bubbleSortMaMe(listaObjetos)

  return listaObjetos
