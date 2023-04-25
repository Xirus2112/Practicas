'''
El signo de * significa que estare pasando mas de un argumento a mi funcion
'''
def suma(*numeros):
    # Inicializo mi variable en cero 
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)
    
suma(1, 2, 3)
suma(150, 259, 1735)
suma(1112321, 123123123, 34543)