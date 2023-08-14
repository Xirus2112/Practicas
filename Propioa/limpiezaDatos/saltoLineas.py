import pandas as pd
import cx_Oracle

# Cargar el archivo Excel
excel_file_path = 'D:/BD_grandesClientes/BD AGRUPADOS 26JUL23.xlsx'
sheet_name = 'BD_AGRUPADOS'
df = pd.read_excel(excel_file_path, sheet_name)

# Función para limpiar los saltos de línea en una celda
def clean_cell(cell_value):
    if isinstance(cell_value, str):
        return cell_value.replace('\n', ' ')
    return cell_value

# Aplicar la función de limpieza a todas las celdas del DataFrame
cleaned_df = df.applymap(clean_cell)

# Convertir columnas específicas a tipo numérico
numeric_columns = ['PAGADOR_OSF', 'PAGADOR_CORRECTO', 'NIC_ASOCIADO', 'PERIODO']
cleaned_df[numeric_columns] = cleaned_df[numeric_columns].apply(pd.to_numeric, errors='coerce')

# Conexión a la base de datos Oracle
db_username = 'MODF_JMARIN'
db_password = 'CALVARADO2022'
db_ip = '10.20.10.58'  
db_port = '1521'  
db_sid = 'CSTDE'

connection = cx_Oracle.connect(f'{db_username}/{db_password}@{db_ip}:{db_port}/{db_sid}')

# Convertir DataFrame a una lista de tuplas
data_to_insert = [tuple(row) for row in cleaned_df.values]

for row in data_to_insert:
    print(row)

# Preparar la consulta de inserción
insert_query = "INSERT INTO nombre_de_la_tabla (PAGADOR_OSF,PAGADOR_CORRECTO,NOMBRE_PAGADOR,IDENTIFICACION_PAGADOR,DIRECCION_ENTREGA,CIUDAD_ENTREGA,EMAIL_FACTURACION,NOMBRE_CONTACTO,TELF_CONTACTO,EJECUTIVO,TIPO_REPARTO,NIC_ASOCIADO,TIPO_AGRUPADO,TIPO_SUMINISTRO,TERRITORIAL,ZONA,DEPARTAMENTO,MUNICIPIO,USO,NOMBRE_NIC,DIR_PREDIO,OBSERVACION,PENDIENTE_COBRO_CORRIENTE,CARTERA,DEUDA_HOY,DEUDA_TOTAL,DEUDA_FINANCIADA,DEUDA_RECLAMADA,PERIODO) VALUES (:1, :2, :3, :4, :5, :6, :7, :8, :9, :10, :11, :12, :13, :14, :15, :16, :17, :18, :19, :20, :21, :22, :23, :24, :25, :26, :27, :28, :29, :30)"

# Ejecutar las inserciones
cursor = connection.cursor()
cursor.executemany(insert_query, data_to_insert)
connection.commit()

# Cerrar la conexión
cursor.close()
connection.close()

print("Proceso completado: Archivo Excel (hoja 'BD_AGRUPADOS') limpiado y datos insertados en la base de datos Oracle.")