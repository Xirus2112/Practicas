import pandas as pd
import numpy as np

# Creando un dataFrame del archivo exportado (Leyendo)

url = "D:/Talend/envioexitoso.csv"
df_leyendo = pd.read_csv(url)


# Montrando las primeas 5 filas del dataFrame
primerasCincoFilas_df = df_leyendo.head()
print("Observando -- Primeras 5 filas del DataFrame")
print(primerasCincoFilas_df)
# Montrando las primeas 5 filas del dataFrame
ultimasCincoFilas_df = df_leyendo.tail()
print("Observando -- Últimas 5 filas del DataFrame")
print(ultimasCincoFilas_df)

# Paramostrar una cantidad especifica solo sele pasa por parametros el numero deseado ejemplo
# ultimasCincoFilas_df = df_leyendo.tail(15) ---> ya sea Tail (ultima) ó head(primeras)

# accediendo al atributo shape --> indica la cantidad de filas y columnas
print("Cnatidad de filas y columnas del DataFrame")
countFile = df_leyendo.shape
print(countFile)

# mostrar "n" filas le pasamos argumentos
pd.set_option('display.max_rows', 50)
print(df_leyendo)



