from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound, HttpResponseRedirect 
from .users_mock import return_user
from restrito.context_processors import lista_turma
# Create your views here.
user = None
def aluno(request):
    return render(request, 'restrito.html')

def professor(request):
    return render(request, 'restrito.html')

def turma(request, perfil, id_turma):
    turmas_dic = lista_turma(request)
    this_turma = None
    for turma in turmas_dic['turmas'] : 
        if id_turma == turma['id']:
            this_turma = turma
    return render(request,'turma.html' , {"turma":this_turma, 'perfil':perfil})

def atividade(request, perfil, id_turma, id_atividade):
    turmas_dic = lista_turma(request)
    this_turma = None
    for turma in turmas_dic['turmas'] : 
        if id_turma == turma['id']:
            this_turma = turma
    this_atividade = None
    for atividade in this_turma['atividades']:
        if int(id_atividade) == int(atividade['id']):
            this_atividade = atividade
    return render(request,'atividade.html', {"atividade":this_atividade})

def restrito(request):
    email = request.POST.get("email")
    senha = request.POST.get("senha")
    user = return_user(email,senha)
    if user:
        turmas_dic = lista_turma(request)
        turmas = []
        for turma in turmas_dic['turmas'] : 
            if user['id'] in turma['users']:
                turmas.append(turma)
        return render(request,'restrito.html', {'turmas':turmas , 'isprofessor':user['isprofessor']})
    else :
        return HttpResponseNotFound('Not Found')