from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import LoginForm, CadastroForm
from .models import Usuario, Tema

def index(request):
    return render(request, 'palavra/index.html')

def entrar(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('jogo')
    else:
        form = LoginForm(request)
    return render(request, 'palavra/login.html', {'form': form})

def cadastrar(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('jogo')
    else:
        form = CadastroForm()
    return render(request, 'palavra/cadastro.html', {'form': form})

@login_required(login_url='/palavra/entrar/')
def jogo(request):
    usuario = request.user
    temas = Tema.objects.all()
    return render(request, 'palavra/jogo.html', {'temas': temas, 'usuario': usuario})

@login_required(login_url='/palavra/entrar/')
def configuracoes(request):
    return render(request, 'palavra/configuracoes.html')

@login_required(login_url='/palavra/entrar/')
def user_info(request):
    user = request.user
    if request.method == 'POST':
        form = UserInfoForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_info')
    else:
        form = UserInfoForm(instance=user)

    return render(request, 'palavra/configuracoes.html', {'form': form})

def mostrar_ranking_melhores(request):
    if not request.user.is_authenticated:
        return redirect('/palavra/entrar/')
    jogadores = Usuario.objects.order_by('-pontuacao_total')[:5]
    return render(request, 'palavra/ranking.html', {'top_cinco': jogadores})