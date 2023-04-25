"""
importamos un modulo llamado math, con la finalidad 
de poder trabajar mejor con la matematicas
https://docs.python.org/es/3/library/math.html
"""
import math
print(round(1.3))
# Extraer el valor absoluto de una operación, el cual (saca) extrae el signo de un nuemero 
print(abs(-55))

print(math.ceil(1.1)) # Incrementea al numero mas cercano
print(math.floor(1.99999)) #lo contrario del de arriba
num1 = 4
num2 = "4"
print(math.isnan(num1)) # como es un numero me retorna el valor False
print(math.pow(10,3)) # Potencia, 10 elevado a la 3
print(round(math.sqrt(6465),0)) # Sacara la raiz cuadrada de un numero