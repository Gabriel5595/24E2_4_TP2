import pandas as pd

def read_csv(file_name):
    path = "C:/Users/gribe/OneDrive/Documentos/Codes/INFNET/2024.1/Python para Dados/TPs/TP2/resources/" + file_name + ".csv"
    dataframe = pd.read_csv(path)
    return dataframe