import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings("ignore")

pd.set_option("display.max_columns", None)

global df_inmuebles, resultados

df_inmuebles = pd.read_csv("data/inmuebles.csv", sep=",")

# print(df_inmuebles.head()) #listar los primeros 5 registros
# print(df_inmuebles.info()) #informacion de las columnas

# cambiar la palabra baño por bano y Área por area
df_inmuebles.columns = df_inmuebles.columns.str.replace("Tipo", "tipo")
df_inmuebles.columns = df_inmuebles.columns.str.replace("Descripcion", "descripcion")
df_inmuebles.columns = df_inmuebles.columns.str.replace("Habitaciones", "habitaciones")
df_inmuebles.columns = df_inmuebles.columns.str.replace("Área", "area")
df_inmuebles.columns = df_inmuebles.columns.str.replace("Baños", "banos")
df_inmuebles.columns = df_inmuebles.columns.str.replace("Barrio", "barrio")
df_inmuebles.columns = df_inmuebles.columns.str.replace("UPZ", "upz")
df_inmuebles.columns = df_inmuebles.columns.str.replace("Valor", "valor")
# eliminar la columna descripcion
df_inmuebles = df_inmuebles.drop(
    columns=["descripcion"]
)  # eliminar la columna descripcion por que no se necesita
df_inmuebles = df_inmuebles.drop(
    columns=["upz"]
)  # eliminar la columna upz por que no se necesita
print(df_inmuebles.columns)  # listar las columnas
# sacar los valores de la columna tipo y listarlos
# print(df_inmuebles.tipo.value_counts()) #listar los valores de la columna tipo
inmuebles_typo = df_inmuebles.tipo.value_counts()

inmuebles_typo.plot.bar()
mostrar = plt.show()
