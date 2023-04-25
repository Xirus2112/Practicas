### Aprendiendo nuevas funciones String ###
texto = "Carlos sabe programar en Python"
# Variables

javascript = "Javascript"
python = "Python"
'''
# IN Evalua si la palabra se encuentra en el texto
print(javascript in texto)
print(python in texto)
'''
#Validando si extisten las variables
'''if javascript in texto:
    print(f"{javascript} es un puen lenguaje")
else:
    print(f"{python} es mucho mejor y me gusta mas")
'''    
# len() indica la cantidad de caracteres
size = len(texto)
print(size)
# upper() utilizado para mayusculas
print(texto.upper())
# lower() utilizado para mayusculas
print(texto.lower())
# count('a') utilizado para mayusculas
print(texto.count('a'))