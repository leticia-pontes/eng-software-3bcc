from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Cadastro, Tema, Palavra
from .login import LoginForm

def index(request):
    lista = Palavra.objects.all()
    contexto = { "lista": lista }
    return render(request, 'palavra/index.html', contexto)

def cadastro(request):
    return render(request, 'palavra/cadastro.html')

def entrar(request):

    if request.method == 'GET':
        formulario = LoginForm()
        return render(request, 'palavra/cadastro.html', {'form': formulario})

    elif request.method == 'POST':
        formulario = LoginForm(request.POST)
        
        if formulario.is_valid():
            usuario = formulario.cleaned_data['usuario']
            senha = formulario.cleaned_data['senha']
            user = authenticate(request,usuario=usuario,senha=senha)
            if user:
                login(request, user)
                return redirect('posts')
        
        messages.error(request,f'Invalid username or password')
        return render(request,'palavra/cadastro.html', {'form': formulario})

def jogo(request):
    return render(request, 'palavra/jogo.html')

def configuracoes(request):
    return render(request, 'palavra/configuracoes.html')

def ranking(request):
    return render(request, 'palavra/ranking.html')