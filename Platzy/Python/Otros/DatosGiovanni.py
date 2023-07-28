import os
import pandas as pd
import glob
import shutil
import tkinter as tk
from tkinter import messagebox


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
    df = df.replace('.', ',')

    # Leer el archivo ProdActualizados_jul2023.csv
    csv_file_path = "//10.20.11.226/Compartida/BASEc/Giovannis/datosCruce/ProdActualizados_jul2023.csv"
    df_csv = pd.read_csv(csv_file_path, sep='|')

    # Convertir la columna 'CUENTA' a tipo str
    df_csv['CUENTA'] = df_csv['CUENTA'].astype(str)

    # Paso 5: Unir internamente las columnas 'NIC' y 'CUENTA' y crear Cruce.xlsx
    df_cruce = pd.merge(df_csv, df, left_on='CUENTA', right_on='NIC', how='inner')

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

def replace_dots_with_commas_in_excel(input_file, output_file):
    # Leer el archivo excel
    df = pd.read_excel(input_file)

    # Aplicar la función lambda para reemplazar puntos por comas en cada celda del DataFrame
    df = df.applymap(lambda x: str(x).replace('.', ','))

    # Convertir columnas numéricas nuevamente a enteros
    numeric_cols = df.select_dtypes(include=[int, float]).columns
    df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors='coerce')

    # Guardar el DataFrame modificado en un nuevo archivo excel
    df.to_excel(output_file, index=False)

def show_information_window(file_path):
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal
    messagebox.showinfo("Proceso finalizado", "El proceso ha finalizado. Haga clic en Aceptar para abrir el archivo generado.")
    root.destroy()  # Cerrar la ventana secundaria

    # Abrir el archivo generado con el programa predeterminado usando os.system()
    os.system(f'start "" "{file_path}"')

if __name__ == "__main__":
    # Especificar la ruta del archivo de entrada "datosCruzados.xlsx"
    input_file_path = "//10.20.11.226/Compartida/BASEc/Giovannis/datosCruzados.xlsx"  # Cambiar por la ruta del archivo a leer

    # Especificar la ruta del archivo de salida "Datos_Giova.xlsx"
    output_file_path = "//10.20.11.226/Compartida/BASEc/Giovannis/Datos_Giova.xlsx"  # Cambiar por la ruta donde deseas guardar el resultado

    # Reemplazar los puntos por comas en el archivo excel y guardar el resultado en "Datos_Giova.xlsx"
    replace_dots_with_commas_in_excel(input_file_path, output_file_path)

    # Mostrar ventana informativa y abrir el archivo generado
    show_information_window(output_file_path)

    # Eliminar el archivo "datosCruzados.xlsx"
    if os.path.exists(input_file_path):
        os.remove(input_file_path)