usuarios = [
    ["Carlos", 4],
    ["Mathias", 1],
    ["Jeremy", 3],
    ["Dilan", 2]
]

"""nombres = []
for usuario in usuarios:
    nombres.append(usuario[0])"""

# Composición
### variable = [expresion for item in items]

"""Tranformacion"""
#nombres = [usuario[0] for usuario in usuarios]

""" Filtrar """
nombres = [usuario for usuario in usuarios if usuario[1] > 2]



print(nombres)