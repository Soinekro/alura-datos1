import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# from google.colab import drive
import warnings

warnings.filterwarnings("ignore")

pd.set_option("display.max_columns", None)

global df_banco, resultados
df_banco = pd.read_csv("data/german_credit.csv", sep=",")
# print(df_banco.head())
# print(df_banco.info())
# print(df_banco.describe())
# print(df_banco.account_check_status.value_counts())
columnas = list(df_banco.select_dtypes(include=["object"]).columns)
for columna in columnas:
    print(f"el nombre de la columna : {columna}")
    print(list(df_banco[f"{columna}"].value_counts().index))
    print("\n")

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
print('\n \n \n')
print(df_banco.head())