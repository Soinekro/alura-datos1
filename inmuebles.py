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

# cambiar la palabra a minuscula y sin caracteres especiales
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
# print(df_inmuebles.columns)  # listar las columnas
# sacar los valores de la columna tipo y listarlos
# print(df_inmuebles.tipo.value_counts()) #listar los valores de la columna tipo

# inmuebles_grap = df_inmuebles.valor.value_counts()  # contar los valores de la columna valor
# inmuebles_grap.plot.bar() # grafico de barras
# plt.title('valor de inmuebles') #titulo del grafico
# plt.show()  # mostrar el grafico

# print(df_inmuebles.valor.value_counts())  # estadisticas de la columna valor

# sumar los valores de la columna valor
# print(df_inmuebles.valor.sum()) # la suma de estos valores es una concatenacion de los valores ya que son de tipo string

# convertir la columna valor a tipo numerico
df_inmuebles.valor = df_inmuebles.valor.str.replace(
    "$", ""
)  # eliminar el signo de dolar
df_inmuebles.valor = df_inmuebles.valor.str.replace(".", "")  # eliminar la coma
# print(df_inmuebles.valor.sum()) # la suma de estos valores es una concatenacion de los valores ya que son de tipo string
df_inmuebles.valor = pd.to_numeric(
    df_inmuebles.valor
)  # convertir la columna valor a tipo numerico
# print(df_inmuebles.valor.sum()) # la suma de estos valores es 5731633605583 que es el valor total de los inmuebles
# checar todos los valores de la columna valor
# print(df_inmuebles.valor)
# mostrar solo columnas tipo, barrio y valor
# df_inmuebles = df_inmuebles[["tipo", "barrio", "valor"]] #mostrar solo columnas tipo, barrio y valor
df_inmuebles.columns = df_inmuebles.columns.str.replace("valor", "precio")
# print(df_inmuebles.describe())
# sacar el precio por metro cuadrado
# df_inmuebles["precio_m2"] = df_inmuebles.precio / df_inmuebles.area
pd.set_option(
    "display.float_format", "{:.2f}".format
)  # formatear los valores de la tabla a 2 decimales redondeados
# print(df_inmuebles.info())
df_inmuebles["precio_millon"] = df_inmuebles["precio"] / 1000000
# df_inmuebles["precio_millon"].plot.hist(bins=10)

# precio de metro cuadrado por barrio
barrio_acumulo = (
    df_inmuebles[["barrio", "precio_millon", "area"]].groupby("barrio").sum()
)
barrio_acumulo["precio_m2"] = barrio_acumulo["precio_millon"] / barrio_acumulo["area"]
# print(df_inmuebles.head())
barrio_x_m2 = barrio_acumulo.reset_index()[["barrio", "precio_m2"]]
top10_desc = (
    barrio_x_m2.sort_values(by="precio_m2", ascending=False)
    .tail(10)
    .sort_values(by="precio_m2", ascending=True)
)
# top10_desc.plot.barh(x="barrio", y="precio_m2").invert_yaxis()  # crear grafico de barras horizontal para los 10 barrios mas baratos
top10_asc = barrio_x_m2.sort_values(by="precio_m2", ascending=False).head(10)
# top10_asc.plot.barh(x="barrio", y="precio_m2").invert_yaxis() # crear grafico de barras horizontal para los 10 barrios mas caros

fig, axs = plt.subplots(1, 2, figsize=(15, 5))


# 10 barrios mas caros
# plt.subplot(1, 2, 1)
axs[0].barh(top10_asc["barrio"], top10_asc["precio_m2"], color="red")
axs[0].invert_yaxis()
axs[0].set_title("Top 10 barrios mas caros")
axs[0].set_xlabel("Precio por metro cuadrado")
axs[0].set_ylabel("Barrio")
for valor, categoria in zip(top10_asc["precio_m2"], top10_asc["barrio"]):
    axs[0].text(valor, categoria, str("%.2f" % valor), ha="left", va="center")

# 10 barrios mas baratos
# plt.subplot(1, 2, 2)
axs[1].barh(top10_desc["barrio"], top10_desc["precio_m2"], color="blue")
axs[1].invert_yaxis()
axs[1].set_title("Top 10 barrios mas baratos")
axs[1].set_xlabel("Precio por metro cuadrado")
axs[1].set_ylabel("Barrio")
for valor, categoria in zip(top10_desc["precio_m2"], top10_desc["barrio"]):
    axs[1].text(valor, categoria, str("%.2f" % valor), ha="left", va="center")
    
plt.tight_layout()
plt.show()
