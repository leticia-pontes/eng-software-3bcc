from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from .models import Usuario, Tema, Palavra
from .forms import LoginForm, CadastroForm

def index(request):
    lista = Palavra.objects.all()
    contexto = { "lista": lista }
    return render(request, 'palavra/index.html', contexto)

def cadastro(request):
    return render(request, 'palavra/cadastro.html')

def entrar(request):

    if request.method == 'POST':

        nome = request.POST['usuario']
        senha = request.POST['senha']

        user = authenticate(request, username=nome, password=senha)
        
        if user is not None:
            login(request, user)
            return redirect('jogo')
        else:
            return render(request, 'palavra/login.html', {'error': 'Usuário ou senha incorretos!'})

    return render(request, 'palavra/login.html')

def cadastrar(request):

    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            senha_criptografada = make_password(cleaned_data['senha'])
            cleaned_data['senha'] = senha_criptografada
            Usuario.objects.create_user(**cleaned_data)
            # form.save()
            return redirect('jogo')
    else:
        form = CadastroForm()
    
    return render(request, 'palavra/cadastro.html', {'form': form})

@login_required(login_url='/entrar/')
def jogo(request):
    
    usuario = None
    if request.user.is_authenticated:
        usuario = Usuario.objects.filter(nome=request.user).first()

    temas = Tema.objects.all()

    return render(request, 'palavra/jogo.html', {'temas': temas, 'usuario': usuario})

@login_required(login_url='/entrar/')
def configuracoes(request):
    return render(request, 'palavra/configuracoes.html')


def mostrar_ranking_melhores(request):
    jogadores = Usuario.objects.all()
    jogadores_filtrados = sorted(jogadores, key=lambda jogador: jogador.pontuacao_total, reverse=True)
    top_cinco = jogadores_filtrados[:5]
    return render(request, 'palavra/ranking.html', {'top_cinco': top_cinco})