# -*- coding: utf-8 -*-
"""Base de datos AV.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RUXvH-ZNb5gSNPFiyd1FjEGvpB_OVtD4
"""

#libreria panda
#comentarios son con #

#imprimir libreria
import pandas as pd

#data frame
df = pd.read_excel("Ventas_Web.xlsx")
#mostrar los primero 5 registros
df.head()

#crear un data frame - para vendedores
df_vendedor = df[["Vendedor"]]
#eliminar los duplicados de la tabla
df_vendedor = df_vendedor.drop_duplicates()
#resetear indice
df_vendedor = df_vendedor.reset_index(drop=True)
#agregar el indice a un campo de la tabla
df_vendedor.reset_index(level=0, inplace=True)
df_vendedor['index']+=1
#que la columna que se llama index se llame id_vendedor
df_vendedor= df_vendedor.rename(columns={'index':'id_vendedor'})
df_vendedor

#crear un data frame - para vendedores
df_producto = df[['Producto', 'Categoría']]
#eliminar los duplicados de la tabla
df_producto = df_producto.drop_duplicates()
#resetear indice
df_producto = df_producto.reset_index(drop=True)
#agregar el indice a un campo de la tabla
df_producto.reset_index(level=0, inplace=True)
df_producto['index']+=1
#que la columna que se llama index se llame id_vendedor
df_producto= df_producto.rename(columns={'index':'id_producto'})
df_producto

#crear un data frame - para vendedores
df_plataforma = df[["Plataforma"]]
#eliminar los duplicados de la tabla
df_plataforma = df_plataforma.drop_duplicates()
#resetear indice
df_plataforma = df_plataforma.reset_index(drop=True)
#agregar el indice a un campo de la tabla
df_plataforma.reset_index(level=0, inplace=True)
df_plataforma['index']+=1
#que la columna que se llama index se llame id_vendedor
df_plataforma= df_plataforma.rename(columns={'index':'id_plataforma'})
df_plataforma

df_ventas=df
df_ventas

df.head()

#print(dataframe)

##Este archivo esta pendiente para su arreglo, ya que todos los datos estan en archivos diferentes

## Get only 'vendedor' data and remove duplicates / Obtener vendedores y borrar duplicados
df_vendedor = df[["Vendedor"]]
df_ventas = pd.merge(df_ventas, df_vendedor, on='Vendedor', how='right')
df_ventas = df_ventas[['Orden','Fecha']]