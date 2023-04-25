# Importamos todos los metodos de la libreria Pandas
import pandas as pd

url = "D:/Users/carlos.alvarado/PycharmProjects/PracticasPy/Datos/DatosPrueba.csv"

# Definimos la matriz de ubicacion del archivo
# df = dataFrame
df = pd.read_csv(url)

# Coloco los nombre de la cabcera
cabecera = ["PassengerId","Survived","Pclass","Name","Sex","Age","SibSp","Parch","Ticket","Fare","Cabin","Embarked"]
#asignamos el valor de la cabecera
df.columns = cabecera
df.head()

#ruta donde enviaremos los datos de pruebas
ruta = "D:/Talend/envioexitoso.csv"
# metodo para envio
df.to_csv(ruta)
