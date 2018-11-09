from django.shortcuts import render
from curriculo.context_processors import lista_cursos
# Create your views here.
def cursos(request,sigla):
    context = filtra_curso(request,sigla)
    return render(request, "curso.html",context)

def disc(request,sigla, disc):
    context = filtra_disc(request, sigla ,disc)
    return render(request, "disciplina.html",context)

def filtra_curso(request,sigla):
    curso = lista_cursos(request)
    for curso_i in curso['cursos']:
        if curso_i['sigla'] == sigla:
            return curso_i

def filtra_disc(request,sigla,disc):
    curso = filtra_curso(request,sigla)
    for disc_ in curso['grade']:
        for dis in disc_['disciplinas']:
            print('CHEGOU', dis)
            if dis['sigla_disc'] == disc:
                return  dis