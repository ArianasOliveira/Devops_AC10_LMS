from django.urls import path
from restrito import views
app_name='restrito'
urlpatterns = [
    path("", views.restrito, name='restrito'),
    path("<str:perfil>/turma/<str:id_turma>/",views.turma, name='turma'),
    path("<str:perfil>/turma/<str:id_turma>/atividade/<str:id_atividade>/",views.atividade, name='atividade'),
]
