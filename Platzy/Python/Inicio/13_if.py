# Condicional IF

'''
    Si se compara con una verificacion True 
    este mostrara el bloque si es falso no lo ara
'''
if True:
    print("Debería ejecurse")
    
if False:
    print("No se ejecurara")
print("-" * 40) 
    
# Ejemplo 1
'''
solicitud = input("¿Cuál es tu mascota favorita? ")

if solicitud == "Perro":
    print(f"El {solicitud} es el favorito de Carlos")
elif solicitud == "Gato":
    print(f"El {solicitud} es el favorito de Jeremy")
elif solicitud == "Pez":
    print(f"El {solicitud} es el favorito de Benjamin")
else:
    print(f"El {solicitud} no entra en la validación")

'''

# Ejemplo 2, validacion numerica
'''
stock = int(input("Digita la cantidad de Stock -> "))

#Validacion
if stock >= 100 and stock <= 300:
    print(f"La cantidad {stock} es considerable.")
else:
    print(f"La cantidad de {stock} no es considerable..!")
'''

# Reto Platzi, Indicar si un numero es par o impar
print("Indicando si el numero es par o impar")
num1 = int(input("Digita el valor del numero que deseas conocer -> "))

result = num1 % 2
print(type(num1))

if (result == 0):
    print("Numero Par :)")
else:
    print("Numero Impar :(")
