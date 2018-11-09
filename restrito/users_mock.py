users = [
        {
            "id": 1,
            "nome": "PEDRO",
            "email": "alunoimpacta@gmail.com",
            "senha": "aluno123",
            "isprofessor": False
        },
        {
            "id": 2,
            "nome": "JUNIOR",
            "email": "professorimpacta@gmail.com",
            "senha": "prof123",
            "isprofessor": True
        }
    ]

def return_user(email,senha):
    for user in users:
        if user['email'] == email and user['senha'] == senha :
            return user
    return None