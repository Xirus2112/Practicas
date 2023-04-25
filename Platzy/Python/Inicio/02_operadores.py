### Operadores ###

# Suma
print(3 + 2)
# Resta
print(3 - 2)
# Multiplicación
print(3 * 2)
# División
print(4 / 2)
# Modulo ó resultado
print(4 % 2)
# Cociente de la división
print(4 // 2)
# Calculando un exponente, 4 elevado a la 2
print(4 ** 2)

# Operaciones con cadenas de texto
print("Hola" > "Python")
print("Hola" < "Python")
print("aaaa" >= "abaa")  # Ordenación alfabética por ASCII
print(len("aaaa") >= len("abaa"))  # Cuenta caracteres
print("Hola" <= "Python")
print("Hola" == "Hola")
print("Hola" != "Python")

# Operadores Logicos
""" Esto es Falso """ 
print(3 > 4 and "Hola" > "Python") 
print(3 > 4 or "Hola" > "Python")
# el NOT se utiliza para NEGAR es decir estaria negando la condición
print(not(3 > 4))

# Formateo

name, surname, age = "Carlos", "Alvarado", 32
print("Mi nombre es {} {} y mi edad es {} años".format(name, surname, age))
