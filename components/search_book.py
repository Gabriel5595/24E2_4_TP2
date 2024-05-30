import pandas

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
            return result
        else:
            return {"erro": "ID não encontrado"}
    
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
        return global_result