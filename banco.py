import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# from google.colab import drive
import warnings

warnings.filterwarnings("ignore")

pd.set_option("display.max_columns", None)

global df_banco, resultados
df_banco = pd.read_csv("data/banco.csv", sep=",")
# print(df_banco.head())
# print(df_banco.info())
# print(df_banco.describe())
# print(df_banco.account_check_status.value_counts())
# columnas = list(df_banco.select_dtypes(include=["object"]).columns)
# for columna in columnas:
#     print(f"el nombre de la columna : {columna}")
#     print(list(df_banco[f"{columna}"].value_counts().index))
#     print("\n")

# print(df_banco.columns)


def procesar_datos():
    global df_banco
    df_banco = df_banco.drop_duplicates() if df_banco.duplicated().any() else df_banco
    df_banco = df_banco.dropna() if df_banco.isnull().values.any() else df_banco

    a = {
        "no checking account": 4,
        ">= 200 DM / salary assignments for at least 1 year": 3,
        "0 <= ... < 200 DM": 2,
        "< 0 DM": 1,
    }
    df_banco["account_check_status"] = df_banco["account_check_status"].map(a)

    b = {
        "no credits taken/ all credits paid back duly": 1,
        "all credits at this bank paid back duly": 2,
        "existing credits paid back duly till now": 3,
        "delay in paying off in the past": 4,
        "critical account/ other credits existing (not at this bank)": 5,
    }
    df_banco["credit_history"] = df_banco["credit_history"].map(b)

    c = {
        "car (new)": 1,
        "car (used)": 2,
        "furniture/equipment": 3,
        "radio/television": 4,
        "domestic appliances": 5,
        "repairs": 6,
        "education": 7,
        "(vacation - does not exist?)": 8,
        "retraining": 9,
        "business": 10,
        "others": 11,
    }
    df_banco["purpose"] = df_banco["purpose"].map(c)

    d = {
        "unknown/ no savings account": 1,
        ".. >= 1000 DM ": 2,
        "500 <= ... < 1000 DM ": 3,
        "100 <= ... < 500 DM": 4,
        "... < 100 DM": 5,
    }
    df_banco["savings"] = df_banco["savings"].map(d)

    e = {
        ".. >= 7 years": 1,
        "4 <= ... < 7 years": 2,
        "1 <= ... < 4 years": 3,
        "... < 1 year ": 4,
        "unemployed": 5,
    }
    df_banco["present_emp_since"] = df_banco["present_emp_since"].map(e)

    f = {
        "male : divorced/separated": 1,
        "female : divorced/separated/married": 2,
        "male : single": 3,
        "male : married/widowed": 4,
        "female : single": 5,
    }
    df_banco["personal_status_sex"] = df_banco["personal_status_sex"].map(f)

    g = {"none": 1, "co-applicant": 2, "guarantor": 3}
    df_banco["other_debtors"] = df_banco["other_debtors"].map(g)

    h = {
        "real estate": 1,
        "if not A121 : building society savings agreement/ life insurance": 2,
        "if not A121/A122 : car or other, not in attribute 6": 3,
        "unknown / no property": 4,
    }
    df_banco["property"] = df_banco["property"].map(h)

    i = {"bank": 1, "stores": 2, "none": 3}
    df_banco["other_installment_plans"] = df_banco["other_installment_plans"].map(i)

    j = {"rent": 1, "own": 2, "for free": 3}
    df_banco["housing"] = df_banco["housing"].map(j)

    k = {
        "unemployed/ unskilled - non-resident": 1,
        "unskilled - resident": 2,
        "skilled employee / official": 3,
        "management/ self-employed/ highly qualified employee/ officer": 4,
    }
    df_banco["job"] = df_banco["job"].map(k)

    l = {"yes, registered under the customers name ": 1, "none": 0}
    df_banco["telephone"] = df_banco["telephone"].map(l)

    m = {"yes": 1, "no": 0}
    df_banco["foreign_worker"] = df_banco["foreign_worker"].map(m)


print(df_banco.head())
procesar_datos()
print("\n \n \n")
# print(df_banco.head())
variables_discretas = [
    "personal_status_sex",
    "age",
    "duration_in_month",
    "credit_amount",
    "default",
]

# print(df_banco[variables_discretas].tail()) #opuesto a head


def feature_engineering():
    global df_banco
    dic_sexo = {2: 1, 5: 1, 1: 0, 3: 0, 4: 0}
    dic_est_civil = {3: 1, 5: 1, 1: 0, 2: 0, 4: 0}
    df_banco["sexo"] = df_banco["personal_status_sex"].map(dic_sexo)
    df_banco["estado_civil"] = df_banco["personal_status_sex"].map(dic_est_civil)
    df_banco["rango_edad"] = pd.cut(
        x=df_banco["age"], bins=[18, 30, 40, 50, 60, 70, 80], labels=[1, 2, 3, 4, 5, 6]
    ).astype(int)
    df_banco["rango_plazos_credito"] = pd.cut(
        x=df_banco["duration_in_month"],
        bins=[1, 12, 24, 36, 48, 60, 72],
        labels=[1, 2, 3, 4, 5, 6],
    ).astype(int)
    df_banco["rango_valor_credito"] = pd.cut(
        x=df_banco["credit_amount"],
        bins=[
            1,
            1000,
            2000,
            3000,
            4000,
            5000,
            6000,
            7000,
            8000,
            9000,
            10000,
            11000,
            12000,
            13000,
            14000,
            15000,
            16000,
            17000,
            18000,
            19000,
            20000,
        ],
        labels=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    ).astype(int)
    df_banco = df_banco.drop(
        columns=["personal_status_sex", "age", "duration_in_month", "credit_amount"]
    )


feature_engineering()
print(df_banco.head())
print(df_banco.describe())

#histograma para la variable edad y la variable sexo
# plt.figure(figsize=(10, 5))
# sns.histplot(df_banco["rango_edad"], kde=True)
# plt.xlabel("Edad")
# plt.ylabel("Frecuencia")
# plt.title("Histograma de la variable edad")
# plt.show()

# plt.figure(figsize=(10, 5))
# sns.histplot(df_banco["sexo"], kde=True)
# plt.xlabel("sexo")
# plt.ylabel("Frecuencia")
# plt.title("Histograma de la variable sexo")
# plt.show()

def analisis_exploratorio():
    global df_banco
    histogramas = ['sexo','estado_civil','rango_plazos_credito','rango_edad','default']
    lista_histogramas = list(enumerate(histogramas)) #enumera la lista
    plt.figure(figsize = (15,8)) #tamaño de la figura
    plt.title('Histogramas') #titulo
    for i in lista_histogramas:
        plt.subplot(3, 2, i[0]+1) #3 filas, 2 columnas, i[0]+1 es la posicion
        sns.countplot(x = i[1], data = df_banco) #i[1] es el nombre de la columna
        plt.xlabel(i[1], fontsize=20) #nombre de la columna
        plt.ylabel('Total', fontsize=20) #nombre del eje y
    #     plt.xticks(fontsize=20)
    plt.show()

analisis_exploratorio()
#1 .analizar los datos de las distribuciones 
# e identificar si hay un valor o registros que no se deben considerar en el analisis
#2. investigar que es un y como crear un mapa de calor
#hacer un mapa de calor para ver la correlacion entre las variables numericas
# crear conclusiones para cada grafico