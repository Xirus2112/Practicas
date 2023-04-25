# Variables
''' La manera correcta de escribir variables es todo en minuscula y separado por guiones bajo'''
my_var_string = "Empesando a ver Variables"
print(my_var_string)

# Variable Entera
my_var_int = 32
my_int_to_str_var = str(my_var_int)
print(my_var_int)

# Variable Flotante
my_variable_float = 32.5
print(my_variable_float)

# Variable Booleana
my_variable_bool = False
print(my_variable_bool)

# Concatenación de variables en un print
print(my_var_string, my_var_int, my_variable_float, my_variable_bool)

# Mostrando cambio de variable
print(type(my_int_to_str_var))

# Entrada de datos con Inputs
nombre = input("¿Cual es tu nombre?")
print(nombre)

# Cambiamos su tipo
name = 35
age = "Brais"
print(name)
print(age)

# ¿Forzamos el tipo?
address: str = "Mi dirección"
address = True
address = 5
address = 1.2
print(type(address))