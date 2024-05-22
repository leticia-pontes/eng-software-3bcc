from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Cadastro, Tema, Palavra

def index(request):
    lista = Palavra.objects.all()
    contexto = { "lista": lista }
    return render(request, 'palavra/index.html', contexto)

def popup(request):
    return render(request, 'palavra/popup.html')

def jogo(request):
    return render(request, 'palavra/jogo.html')

def configuracoes(request):
    return render(request, 'palavra/configuracoes.html')