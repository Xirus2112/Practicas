# Practica
x = 3.3
y = 1.1 + 2.2

print(x)
print(y)
# 1era Prueba de comparación
print(x == y)
print("-" * 50)
# Por cuestiones de referenciacion de memoria, y operacion de python 
'''
    Existen dos maneras de realizar la operación
'''
# Forma de los String
y_str = format(y, ".2g")
print("Convirtiendo a Str ->", y_str)
print(y_str == str(x))
print("-" * 50)
# Forma Matematica
tolerance = 0.00001
# Valor Absoluto
'''
    Se resta para que de siempre valores positivos
'''
print(abs(x - y) < tolerance)
