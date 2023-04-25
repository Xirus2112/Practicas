"""
Proyecto Calculadora
"""
n1 = int(input("Ingresa el primer numero "))
n2 = int(input("Ingresa el segundo numero "))

suma = n1 + n2
resta = n1 - n2
multi = n1 * n2
div = n1 // n2

resultado = f"""
para los resultado de la operanión entre {n1} y {n2}, 
los resultados de la suma son: {suma}
los resultados de la resta son: {resta}
los resultados de la multiplicación son: {multi}
los resultados de la división son: {div}
"""
print(resultado)