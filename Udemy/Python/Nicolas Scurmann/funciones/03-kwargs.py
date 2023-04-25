# KWARGS = KeyWord Argumento
def get_product(**datos):
    print(datos["id"], datos["name"])
    
get_product(id = "23",
            name = "Xiaomi",
            desc = "Esto es un telefono xiaomi"
            )