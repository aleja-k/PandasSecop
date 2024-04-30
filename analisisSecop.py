import pandas as pd

# Leer excel
archivo_excel = "C:/Users/Administrador/Desktop/practicas/SECOP_exported_1.csv"
df = pd.read_excel(archivo_excel)

# Imprimir una muestra de los datos en las columnas problemáticas
print("\nMuestra de datos en las columnas 'PAIS', 'DIRECCION_EJECUCION', 'PAA', y 'MISION_VISION':")
print(df[['PAIS', 'DIRECCION_EJECUCION', 'PAA', 'MISION_VISION']].head())

# Mostrar las primeras filas
print("Primeras filas del archivo:")
print(df.head())

# Calcular algunas estadísticas básicas
print("\nEstadísticas básicas:")
print(df.describe())

# Verificar los tipos de datos de las columnas
print("\nTipos de datos de las columnas:")
print(df.dtypes)

# Contar los valores únicos en una columna
columna = 'ESTADO'  
print("\nValores únicos en la columna '{}':".format(columna))
print(df[columna].nunique())

# Agregar las columnas necesarias al DataFrame
columnas_extra = ['PAIS', 'DIRECCION_EJECUCION', 'PAA', 'MISION_VISION']
for columna in columnas_extra:
    if columna not in df.columns:
        df[columna] = None  # Puedes asignar un valor por defecto si lo deseas

# Mostrar las columnas actualizadas
print("\nColumnas actualizadas:")
print(df.columns)


# Mostrar todas las columnas del DataFrame
print("Todas las columnas del archivo:")
print(df)

# Imprimir valores únicos en la columna 'PAA'
print("\nValores únicos en la columna 'PAA':")
print(df['PAA'].unique())

# Filtrar datos y agregar columnas
valores = ["Publicado", "Proceso en evaluación y observaciones"]
columnas = ['ESTADO','TIPO_PROCESO', 'VALOR_ESTIMADO', 'PAIS', 'ENTIDAD_ESTATAL', 'FASE_ACTUAL', 'FECHA_PRESENTACION', 'DESCRIPCION_CONTRATO', 'FECHA_TERMINACION', 'DIRECCION_EJECUCION','PAA']
datos_filtrados = df

#[(df['ESTADO'].isin(valores)) & ((df['PAA'].astype(str).str.strip() != '') | (df['PAA'].isnull()))][columnas]



# Mostrar los datos filtrados
print("\nDatos filtrados:")
print(datos_filtrados)

# Guardar el DataFrame modificado en un nuevo archivo Excel
archivo_salida = "C:/Users/Administrador/Downloads/DaframeSECOP.xlsx"
datos_filtrados.to_excel(archivo_salida, index=False)
