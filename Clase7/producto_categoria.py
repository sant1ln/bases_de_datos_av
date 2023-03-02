import pandas as pd

## Load file in dataframe | Cargar archivo en dataframe
file_location = './Ventas_Web.xlsx'
dataframe = pd.read_excel('./Ventas_Web.xlsx')
##print(dataframe)

## Get only 'producto' data and remove duplicates / Obtener productoes y borrar duplicados
dataframe_producto = dataframe[['Producto', 'Categoría']]
dataframe_producto = dataframe_producto.drop_duplicates()
##print(dataframe_producto)

##Reset index 
dataframe_producto = dataframe_producto.reset_index(drop=True)
##print(dataframe_producto)

##Add index as table value / Añadir indice como campo de la tabla
dataframe_producto.reset_index(level=0, inplace=True)
##print(dataframe_producto)

##Increment index / Aumentar en uno el indice
dataframe_producto['index'] += 1
##print(dataframe_producto)

##Rename columname
dataframe_producto = dataframe_producto.rename(columns={'index':'id_producto'})
print(dataframe_producto)