def lista_cursos(request):
    return {
        "cursos":[
            {
                "nome":"Sistemas da Informação", 
                "sigla":"SI",
                "coord": "Ana Cris",
                "descricao":" descrição 1",
                "grade":[
                    {
                        "semestre": "1° semestre",
                        "disciplinas": [
                            {
                                "nome":"Materia SI1S",
                                "sigla_disc" :"t1",
                                "ementa":"CONTEUDO"
                            },
                            {
                                "nome":"Materia SI1S",
                                "sigla_disc" :"t2",
                                "ementa":"CONTEUDO"
                            },
                            {
                                "nome":"Materia SI1S",
                                "sigla_disc" :"t3",
                                "ementa":"CONTEUDO"
                            }
                        ]
                    },
                    {
                        "semestre": "2° semestre",
                        "disciplinas": [
                            {
                                "nome":"Materia SI2S",
                                "sigla_disc" :"t1",
                                "ementa":"CONTEUDO"
                            },
                            {
                                "nome":"Materia SI2S",
                                "sigla_disc" :"t2",
                                "ementa":"CONTEUDO"
                            },
                            {
                                "nome":"Materia SI2S",
                                "sigla_disc" :"t3",
                                "ementa":"CONTEUDO"
                            }
                        ]
                    }
                ]
            },
            {
                "nome":"Análise e Desenvolvimento de Sistemas", 
                "sigla":"ADS",
                "coord": "Ana Cris",
                "descricao":" descrição 2",
                "grade":[
                    {
                        "semestre": "1° semestre",
                        "disciplinas": [
                            {
                                "nome":"Materia ADS1",
                                "sigla_disc" :"t1",
                                "ementa":"CONTEUDO"
                            },
                            {
                                "nome":"Materia ADS1",
                                "sigla_disc" :"t2",
                                "ementa":"CONTEUDO"
                            },
                            {
                                "nome":"Materia ADS1",
                                "sigla_disc" :"t3",
                                "ementa":"CONTEUDO"
                            }
                        ]
                    },
                    {
                        "semestre": "2° semestre",
                        "disciplinas": [
                            {
                                "nome":"Materia ADS2",
                                "sigla_disc" :"t1",
                                "ementa":"CONTEUDO"
                            },
                            {
                                "nome":"Materia ADS2",
                                "sigla_disc" :"t2",
                                "ementa":"CONTEUDO"
                            },
                            {
                                "nome":"Materia ADS2",
                                "sigla_disc" :"t3",
                                "ementa":"CONTEUDO"
                            }
                        ]
                    }
                ]
            },
            {
                "nome":"Banco de Dados", 
                "sigla":"BD",
                "coord": "Gustavo Ferreira",
                "descricao":" descrição 3",
                "grade":[
                    {
                        "semestre": "1° semestre",
                        "disciplinas": [
                            {
                                "nome":"Materia BD1S",
                                "sigla_disc" :"t1",
                                "ementa":"CONTEUDO"
                            },
                            {
                                "nome":"Materia BD1S",
                                "sigla_disc" :"t2",
                                "ementa":"CONTEUDO"
                            },
                            {
                                "nome":"Materia BD1S",
                                "sigla_disc" :"t3",
                                "ementa":"CONTEUDO"
                            }
                        ]
                    },
                    {
                        "semestre": "2° semestre",
                        "disciplinas": [
                            {
                                "nome":"Materia BD2S",
                                "sigla_disc" :"t1",
                                "ementa":"CONTEUDO"
                            },
                            {
                                "nome":"Materia BD2S",
                                "sigla_disc" :"t2",
                                "ementa":"CONTEUDO"
                            },
                            {
                                "nome":"Materia BD2S",
                                "sigla_disc" :"t3",
                                "ementa":"CONTEUDO"
                            }
                        ]
                    }
                ]
            }
        ]
    }