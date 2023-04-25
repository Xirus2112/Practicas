### Juego de Piedra, Papel, Tijeras ####
print("Elige una de las opciones (Piedra - Papel - Tijera) ")
user_option = input("Usuario elige => ")

# Opcion del pc
computer_option = "Papel"


# Validación 
if user_option == computer_option:
    print(f"Usuario elige: {user_option} PC elige: {computer_option}, Quedán Empatados")
elif user_option == "Piedra":
    if computer_option == "Tijera":
        print("Piedra gana a Tijera")
        print("El USUARIO es el GANADOR")
    else:
        print("Papel gana a Piedra")
        print("El COMPUTADOR es el GANADOR")
elif user_option == "Papel":
    if computer_option == "Piedra":
        print("Papel gana a Piedra")
        print("El USUARIO es el GANADOR")
    else:
        print("Tijera gana a Papel")
        print("El COMPUTADOR es el GANADOR")
elif user_option == "Tijera":
    if computer_option == "Papel":
        print("Tijera gana a Papel")
        print("El USUARIO es el GANADOR")
    else:
        print("Piedra gana a Tijera")
        print("El COMPUTADOR es el GANADOR")