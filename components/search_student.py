import pandas

def search_student(dataframe, term, is_ra=None):
    if is_ra:
        student = dataframe[dataframe['num_ra'] == term]
        if not student.empty:
            student_dict = student.iloc[0].to_dict()
            result = {
                "registro": student_dict["num_ra"],
                "nome": student_dict["nome"],
                "curso": student_dict["curso"],
                "semestre": student_dict["semestre"],
                "livros": {}
            }
            books = {f"livro {i+1}": student_dict.pop(f"livro_{i+1}") for i in range(3)}
            result["livros"] = books
            return result
        else:
            return {"erro": "RA não encontrado"}
    
    else:
        students = dataframe[dataframe["nome"].str.contains(term, case=False, na=False)]
        result = {
            "registros_encontrados": len(students),
            "alunos": {}
            }
        for index, student in enumerate(students.iterrows()):
            students_data = student[1].to_dict()
            # Agrupar os livros em um subdicionário "livros"
            books = {f"livro {i+1}": students_data.pop(f"livro_{i+1}") for i in range(3)}
            students_data["livros"] = books
            result["alunos"][f"aluno_{index+1}"] = students_data
        return result