import pandas
import sys
import os
# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from components.read_csv import read_csv

def search_book(dataframe, term, is_id=None):
    if is_id:
        book = dataframe[dataframe["id"] == term]
        if not book.empty:
            book_dict = book.iloc[0].to_dict()
            result = {
                "id": book_dict["id"],
                "codigo": book_dict["codigo"],
                "titulo": book_dict["titulo"],
                "autores": {},
                "volume": book_dict["volume"],
                "aluno": book_dict["aluno"]
            }
            authors = {f"autor {i+1}": book_dict.pop(f"autor_{i+1}") for i in range(3)}
            result["autores"] = authors
            return pandas.Series(result).to_json(orient="index", indent=4, force_ascii=False)
        else:
            return pandas.Series({"erro": "ID não encontrado"}).to_json(orient='index', indent=4, force_ascii=False)
    
    else:
        books = dataframe[dataframe["titulo"].str.contains(term, case=False, na=False)]
        global_result = {
            "registros_encontrados": len(books),
            "livros": {}
            }
        for index, book in enumerate(books.iterrows()):
            books_data = book[1].to_dict()
            result = {
                "id": books_data["id"],
                "codigo": books_data["codigo"],
                "titulo": books_data["titulo"],
                "autores": {},
                "volume": books_data["volume"],
                "aluno": books_data["aluno"]
            }
            # Agrupar os livros em um subdicionário "livros"
            authors = {f"autor {i+1}": books_data.pop(f"autor_{i+1}") for i in range(3)}
            result["autores"] = authors
            global_result["livros"][f"livro_{index+1}"] = result
        return pandas.Series(global_result).to_json(orient='index', indent=4, force_ascii=False)

def main():
    dataframe = read_csv("db_books")
    print("***TESTE ID***")
    print(search_book(dataframe, 20, is_id=True))
    print()
    print("***TESTE TITULO***")
    print(search_book(dataframe, "Matematica Basica", is_id=False))
    print()

main()