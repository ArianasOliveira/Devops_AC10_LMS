def lista_turma(request):
    return { "turmas":[
        {
            "id": "ADS-2D",
            "periodo": "noturno",
            "users": [2,1],
            "atividades": [
               {
                "id":1,
                "descricao":"descricao",
                "comentario":"Conteudo"
                },
                {
                "id":2,
                "descricao":"descricao",
                "comentario":"Conteudo"
                }
            ]
        },
        {
            "id": "ADS-3D",
            "periodo": "noturno",
            "users": [2],
            "atividades": [
                {
                "id":1,
                "descricao":"Conteudo-teste",
                "comentario":"Conteudo"
                },
                {
                "id":2,
                "descricao":"Conteudo-teste",
                "comentario":"Conteudo"
                }
            ]
        },
    ]}