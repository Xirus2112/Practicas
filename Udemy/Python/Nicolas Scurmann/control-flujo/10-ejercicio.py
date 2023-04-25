# Calculadora v2
# Realiza una calculadora donde tengas que pasar los valores, y la operacion
# finalmente el valor lo tomara como primer ejemplo para los siguientes calculos
mensaje = """
    Bienvenido a la calculadora. Por favor ten encuenta lo siguiente:
        1.- Para salir, solo escribe "Salir"
        2.- Las operaciones son:
            2.1.- suma
            2.2.- rest
            2.3.- mult
            2.4.- divi
"""
print(mensaje)

resultado = ""
while True:
    if not resultado:
        resultado = input("Ingrese número: ")
        if resultado.lower() == "salir":
            break
        resultado = int(resultado)
    op = input("Ingresa la operación: ")
    if op.lower() == "salir":
        break
    n2 = input("Ingresa siguiente valor: ")
    if n2.lower() == "salir":
        break
    n2 = int(n2)

    if op.lower() == "suma":
        resultado += n2
    elif op.lower() == "rest":
        resultado -= n2
    elif op.lower() == "mult":
        resultado *= n2
    elif op.lower() == "divi":
        resultado /= n2
    else:
        print("Operación no valida")
        break
    print(f"El resultado es: {resultado}")