import os
import pandas as pd

ruta = r'\\10.20.11.226\Compartida\BASEc\DimensionamientoOperativo'
archivo_lecta_unificado = 'LECTA_UNIFICADO.xlsx'
archivo_pyg_unificado = 'PYG_UNIFICADO.xlsx'

archivos_lecta = []
archivos_pyg = []

# Obtener los nombres de los archivos en la ruta especificada
for archivo in os.listdir(ruta):
    if archivo.startswith('LECTA') and archivo.endswith('.xlsx'):
        archivos_lecta.append(os.path.join(ruta, archivo))
    elif archivo.startswith('PYG') and archivo.endswith('.xlsx'):
        archivos_pyg.append(os.path.join(ruta, archivo))

# Unificar archivos de lecta
if archivos_lecta:
    datos_lecta = pd.DataFrame()
    for archivo in archivos_lecta:
        hojas = pd.read_excel(archivo, sheet_name=None)
        if 'Plantilla Dimen. Oper.' in hojas:
            datos_hoja = hojas['Plantilla Dimen. Oper.']
            datos_lecta = pd.concat([datos_lecta, datos_hoja], ignore_index=True)

    # Guardar el archivo unificado de lecta
    if not datos_lecta.empty:
        datos_lecta.to_excel(os.path.join(ruta, archivo_lecta_unificado), index=False)

# Unificar archivos de pyg
if archivos_pyg:
    datos_pyg = pd.DataFrame()
    for archivo in archivos_pyg:
        hojas = pd.read_excel(archivo, sheet_name=None)
        if 'Plantilla Dimen. Oper.' in hojas:
            datos_hoja = hojas['Plantilla Dimen. Oper.']
            datos_pyg = pd.concat([datos_pyg, datos_hoja], ignore_index=True)

    # Guardar el archivo unificado de pyg
    if not datos_pyg.empty:
        datos_pyg.to_excel(os.path.join(ruta, archivo_pyg_unificado), index=False)
