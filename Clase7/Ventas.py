import pandas as pd

## Load file in dataframe | Cargar archivo en dataframe
file_location = './Ventas_Web.xlsx'
dataframe = pd.read_excel('./Ventas_Web.xlsx')
##print(dataframe)

##Este archivo esta pendiente para su arreglo, ya que todos los datos estan en archivos diferentes

## Get only 'vendedor' data and remove duplicates / Obtener vendedores y borrar duplicados
dataframe_vendedor = dataframe[['Vendedor']]
dataframe_ventas = pd.merge(df_ventas, df_vendedor, on='Vendedor', how='right')
df_ventas = df_ventas[['Orden','Fecha','Medio','id_vendedor','plataforma','Comisión', 'Tipo Orden', 'Tipo de Cliente', 'Sexo', 'Categoría', 'Producto', 'Precio']]

