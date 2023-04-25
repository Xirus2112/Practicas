# Contextos globales de la funcion, el alcance de la variable estara dentro de la propia funcion
# Varibles globales son malas practicas
# para usar una variable global si es que realmente se necesita, ps se antepone la palabra recervada GLOBAL
saludo = "Hola Carlos"

def saludar():
    global saludo
    saludo = "Hola Mundo"
    print(saludo)
    
def saludChanchito():
    saludo = "Hola Chanchito"
    print(saludo)

print(saludo)    
saludar()


"""

        NO USAR VARIABLES GLOBALES

"""