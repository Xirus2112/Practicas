"""
Comprar una entrada al cine, sin embargo la pelicula es para mayor de 18 años
sin embargo se podra obtener un descuento si el usuario es mayor a 55 años
"""

edad = 102

if edad < 18:
    print("El es menor de edad")
elif edad >= 18 and edad <55:
    print("Puedes ver la pelicula sin descuento")
elif edad >= 55 and edad < 101:
    print("El puede ver la pelucula y a la vez obtiene un descuento")
else:
    print("No puede tener mas de 100 años")