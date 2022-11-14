class Articulo: 

  def __init__(self , nombre , precio): 
    self.nombre = nombre 
    self.precio = precio


a1 = Articulo("articulo1" , 10)
a2 = Articulo("articulo2" , 7)
a3 = Articulo("articulo3" , 5)
a4 = Articulo("articulo4" , 8)
a5 = Articulo("articulo5" , 24)

#ordenar en una lista de mayor a menor 
AA = [a1 , a2 , a3 , a4 , a5]

print("==============NORMAL==============")

for i in range(len(AA)): 
    print(AA[i].nombre + " " + str(AA[i].precio) )

print("==========MENOR A MAYOR==========")

def bubbleSortMeMa(AA): 
  intercambio = True 

  while intercambio: 
    intercambio = False
    for i in range(len(AA) -1): 
      if(AA[i].precio > AA[i+1].precio):
        #intercambiamos los datos
        AA[i] , AA[i+1] = AA[i+1] , AA[i]
        intercambio = True
  return AA 

AA = bubbleSortMeMa(AA)

for i in range(len(AA)): 
    print(AA[i].nombre + " " + str(AA[i].precio))

print("=========MAYOR A MENOR===========")

def bubbleSortMaMe(AA): 
  intercambio = True 

  while intercambio: 
    intercambio = False
    for i in range(len(AA) -1): 
      if(AA[i].precio < AA[i+1].precio):
        #intercambiamos los datos
        AA[i] , AA[i+1] = AA[i+1] , AA[i]
        intercambio = True
  return AA 

AA = bubbleSortMaMe(AA)

for i in range(len(AA)): 
    print(AA[i].nombre + " " + str(AA[i].precio))

print("====================")
