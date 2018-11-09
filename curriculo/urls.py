from django.urls import path
from curriculo import views

app_name='curriculo'
urlpatterns = [
    path("<str:sigla>/",views.cursos, name='curso'),
    path("<str:sigla>/disciplina/<str:disc>/",views.disc, name='disciplina')
]
