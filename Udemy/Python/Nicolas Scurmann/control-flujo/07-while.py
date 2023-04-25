# numero = 1
# while numero < 100:
#    print(numero)
#    numero *= 2

#comando = ""
#while comando != "salir":
 ##  print(comando)

# Loops infinitos, podemos definirlo con un if para cerrar el ciclo

while True:
    comando = input("$ ")
    print(comando)
    if comando.lower() == "salir":
        break