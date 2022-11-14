#########=================================== CLASES ===================================#########
class Articulo: 

  def __init__(self , nombre , precio, estrellas): 
    self.nombre = nombre 
    self.precio = precio
    self.estrellas = estrellas
    
    if(estrellas !=  "Este producto aun no tiene reseñas"):
      print("=========si tiene reseñas=========")
      if( float(precio) >= 1500 and float(estrellas) >= 4): rec = "Es algo caro pero es de buena calidad"
      if( float(precio) <= 1500 and float(estrellas) >= 4): rec = "Es un buen precio para su calidad"
      if( float(estrellas) ==5): 
        if( float(precio) >= 1500): rec = "Es caro pero es un buen producto"
        elif( float(precio)< 1500): rec = "Es de las mejores opciones"
      if( float(estrellas) < 4): 
        if( float(precio) >= 1500): rec = "Es muy caro para su baja calidad"
        elif( float(precio)<= 1500 and float(precio) > 1000): rec = "Es caro para su baja calidad"
        elif( float(precio) <= 1000): rec = "Es barato pero no es de muy buena calirar calidad"
    else:
      print(estrellas) 
      rec = estrellas 
      
    
    self.recomendacion = rec