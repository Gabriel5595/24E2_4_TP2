import pandas
from datetime import datetime
import sys
import os
# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from components.read_csv import read_csv
from components.search_book import search_book
from components.search_student import search_student

def generate_json(data, file_name=None):
    # Se o nome_arquivo for None, gerar um nome baseado na data e hora
    if file_name is None:
        actual_date_time = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_name = f"{actual_date_time}_file"
    
    # Construir o caminho completo do arquivo
    path = "C:/Users/gribe/OneDrive/Documentos/Codes/INFNET/2024.1/Python para Dados/TPs/TP2/resources/" + file_name + ".json"
    
    print(data)
    dataframe = pandas.DataFrame.from_dict(data)
    print(dataframe)
    dataframe.to_json(path, orient='index', force_ascii=False, indent=4)
    print(data)

def main():
    dataframe = read_csv("db_students")
    data = search_student(dataframe, "Ana", )
    generate_json(data)

main()