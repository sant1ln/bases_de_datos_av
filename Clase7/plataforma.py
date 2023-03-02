import pandas as pd

## Load file in dataframe | Cargar archivo en dataframe
file_location = './Ventas_Web.xlsx'
dataframe = pd.read_excel('./Ventas_Web.xlsx')
##print(dataframe)

## Get only 'plataforma' data and remove duplicates / Obtener plataformaes y borrar duplicados
dataframe_plataforma = dataframe[['plataforma']]
dataframe_plataforma = dataframe_plataforma.drop_duplicates()
##print(dataframe_plataforma)

##Reset index 
dataframe_plataforma = dataframe_plataforma.reset_index(drop=True)
##print(dataframe_plataforma)

##Add index as table value / Añadir indice como campo de la tabla
dataframe_plataforma.reset_index(level=0, inplace=True)
##print(dataframe_plataforma)

##Increment index / Aumentar en uno el indice
dataframe_plataforma['index'] += 1
##print(dataframe_plataforma)

##Rename columname
dataframe_plataforma = dataframe_plataforma.rename(columns={'index':'id_producto'})
print(dataframe_plataforma)