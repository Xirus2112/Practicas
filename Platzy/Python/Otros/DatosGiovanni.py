import os
import pandas as pd
import glob
import shutil


def move_and_clean_excel_file():
    # Paso 1: Buscar y seleccionar XLSX
    file_list = glob.glob("C:/Users/carlos.alvarado/Air-e SAS ESP/Jhon Sebastian Garces - LECTURAS DIARIAS AMI/*.xlsx")
    if not file_list:
        print("No se encontraron archivos .xlsx en la carpeta actual.")
        return

    excel_file = file_list[0]

    # Definir la nueva ruta y nombre del archivo
    new_path = "//10.20.11.226/Compartida/BASEc/Giovannis/datos.xlsx"

    # Cerrar el archivo antes de copiarlo
    try:
        excel_file.close()
    except AttributeError:
        pass

    # Copiar el archivo a la nueva ubicación
    shutil.copyfile(excel_file, new_path)

    # Leer el archivo excel
    df = pd.read_excel(new_path)

    # Paso 2: Eliminar registros con letras o caracteres especiales en la columna A
    df = df[df['NIC'].apply(lambda x: str(x).isalnum())]

    # Convertir la columna 'NIC' a tipo str
    df['NIC'] = df['NIC'].astype(str)

    # Paso 3: Reemplazar puntos por comas en todas las columnas
    df = df.applymap(lambda x: x.replace('.', ','))

    # Leer el archivo ProdActualizados_jul2023.csv
    csv_file_path = "//10.20.11.226/Compartida/BASEc/Giovannis/datosCruce/ProdActualizados_jul2023.csv"
    df_csv = pd.read_csv(csv_file_path, sep='|')

    # Convertir la columna 'CUENTA' a tipo str
    df_csv['CUENTA'] = df_csv['CUENTA'].astype(str)

    # Paso 5: Unir internamente las columnas 'NIC' y 'CUENTA' y crear Cruce.xlsx
    df_cruce = pd.merge(df, df_csv, left_on='NIC', right_on='CUENTA', how='inner')

    # Guardar el resultado en un nuevo archivo excel
    result_path = "//10.20.11.226/Compartida/BASEc/Giovannis/Cruce.xlsx"
    df_cruce.to_excel(result_path, index=False)


if __name__ == "__main__":
    move_and_clean_excel_file()

def filter_and_save_data():
    # Leer el archivo "Cruce.xlsx"
    cruce_path = "//10.20.11.226/Compartida/BASEc/Giovannis/Cruce.xlsx"
    df_cruce = pd.read_excel(cruce_path)

    # Filtrar las filas con "ATL NORTE" o "ATL SUR" en la columna "TERRITORIAL"
    territoriales_filtradas = ["ATL NORTE", "ATL SUR"]
    df_filtrado = df_cruce[df_cruce['TERRITORIAL'].isin(territoriales_filtradas)]

    # Guardar el resultado en un nuevo archivo excel llamado "datosCruzados.xlsx"
    datos_cruzados_path = "//10.20.11.226/Compartida/BASEc/Giovannis/datosCruzados.xlsx"
    df_filtrado.to_excel(datos_cruzados_path, index=False)

    # Eliminar el archivo "Cruce.xlsx"
    os.remove(cruce_path)

if __name__ == "__main__":
    filter_and_save_data()