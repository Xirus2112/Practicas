import random

# Definimos las opciones de juego
opciones = ["piedra", "papel", "tijeras"]

# Pedimos al usuario que elija una opción
jugador = input("Elige piedra, papel o tijeras: ").lower()

# Elegimos una opción aleatoria para la computadora
computadora = random.choice(opciones)

# Imprimimos las opciones elegidas
print("Jugador: " + jugador)
print("Computadora: " + computadora)

# Comprobamos quién ganó
if jugador == computadora:
    print("Empate")
elif jugador == "piedra":
    if computadora == "papel":
        print("La computadora gana")
    else:
        print("El jugador gana")
elif jugador == "papel":
    if computadora == "tijeras":
        print("La computadora gana")
    else:
        print("El jugador gana")
elif jugador == "tijeras":
    if computadora == "piedra":
        print("La computadora gana")
    else:
        print("El jugador gana")
else:
    print("Opción inválida. Elige piedra, papel o tijeras.")
