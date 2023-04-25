# Mi primera funcion

def hola(nombre, apellido="Apellido"): # se coloca el igual apellido para que por defecto lo tome y no nos arroje error
    print(f"Hola {nombre} {apellido}")
    print("Como estas?")
# el valor agredo es para obtener funciones con parametros opcionales
nombre = input("Digita el nombre: ")
apellido = input("Digita el apellido: ")
hola(nombre, apellido)

# Parametros Opcionales
hola(nombre)

# Parametros renombrados
hola(apellido="Alvarado", nombre="Jeremy")