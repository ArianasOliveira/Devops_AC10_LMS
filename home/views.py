from django.shortcuts import render , render_to_response
from django.template.loader import get_template

from .forms import LoginForm
from django.http import HttpResponseRedirect
 

# Create your views here.
def home(request):
    return render(request, "home.html")

def entrar(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/restrito')
    else:
        form = LoginForm()
    return render(request, "login.html", {'form':form})

def contato(request):
    return render(request, "contato.html")
