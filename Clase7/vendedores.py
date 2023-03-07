import pandas as pd

## Load file in dataframe | Cargar archivo en dataframe
file_location = './Ventas_Web.xlsx'
dataframe = pd.read_excel('./Ventas_Web.xlsx')
##print(dataframe)

## Get only 'vendedor' data and remove duplicates / Obtener vendedores y borrar duplicados
dataframe_vendedor = dataframe[['Vendedor']]
dataframe_vendedor = dataframe_vendedor.drop_duplicates()
##print(dataframe_vendedor)

##Reset index 
dataframe_vendedor = dataframe_vendedor.reset_index(drop=True)
##print(dataframe_vendedor)

##Add index as table value / Añadir indice como campo de la tabla
dataframe_vendedor.reset_index(level=0, inplace=True)
##print(dataframe_vendedor)

##Increment index / Aumentar en uno el indice
dataframe_vendedor['index'] += 1
##print(dataframe_vendedor)

##Rename columname
dataframe_vendedor = dataframe_vendedor.rename(columns={'index':'id_producto'})
""" print(dataframe_vendedor) """