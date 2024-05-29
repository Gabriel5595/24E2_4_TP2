import pandas as pd
import sys
import os
# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def read_csv(file_name):
    path = "C:/Users/gribe/OneDrive/Documentos/Codes/INFNET/2024.1/Python para Dados/TPs/TP2/resources/" + file_name + ".csv"
    dataframe = pd.read_csv(path)
    return dataframe

def main():
    print(read_csv("db_books"))
    print(read_csv("db_students"))

main()