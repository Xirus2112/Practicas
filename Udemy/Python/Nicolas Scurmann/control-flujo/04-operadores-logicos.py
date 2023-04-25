"""
Operadores Logicos mas utilizados
and , or , not
"""

# Ejemplo 1
gas = True
encendido = True
edad = 18

if gas and encendido:
    print("Puedes avanzar")
else:
    print("Quedas detenido")

# Ejemplo 2
gas = True
encendido = False

if gas or  encendido:
    print("Puedes avanzar")
else:
    print("Quedas detenido")

# Not es para negar si algo esta falso lo pasara a positivo y viceversa

if not gas and (encendido or edad > 17):
    print("Puedes Avanzar")

"""
Operador de corto circuito, es el que va a depender del operador con el cual nosotros estemos trabjando, 
y esto con la finalidad de que si el operador a la izquierda segun el flujo de ejecucion es falso el no
tendra en cuenta los demas condicionales. Esto con la finalidad de ahorrar recursos en el pc esto para el 
AND pero si es para el OR el aunque el primero sea falso el si revisara el segundo operador
"""