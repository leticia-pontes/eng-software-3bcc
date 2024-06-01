# Autenticação de Usuário
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import LoginForm, CadastroForm, UserInfoForm
from django.views.decorators.csrf import csrf_exempt

# Renderização do models nas views
from .models import Usuario, Tema, Palavra
from django.http import JsonResponse
import json

# Lógica do Jogo
from .termo import Termo, InvalidAttempt
import random
# import logging

# logger = logging.getLogger(__name__)

# Página Inicial
def index(request):
    return render(request, 'palavra/index.html')

# Autenticação
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


# Jogabilidade
def get_palavra_aleatoria():
    palavra_aleatoria = Palavra.objects.order_by('?').first()
    return palavra_aleatoria.word if palavra_aleatoria else None

@login_required(login_url='/palavra/entrar/')
@csrf_exempt
def jogo(request):
    usuario = request.user
    temas = Tema.objects.all()
    
    if request.method == 'POST':
        dados = json.loads(request.body)
        palavra = get_palavra_aleatoria()
        
        # if palavra:
        #     termo = Termo(palavra, {palavra})
        #     try:
        #         result = termo.test(dados.get('palavra', ''))
        #     except InvalidAttempt as e:
        #         logger.error(f"InvalidAttempt exception: {e}")
        
        # return JsonResponse({'status': 'success'})

    return render(request, 'palavra/jogo.html', {'temas': temas, 'usuario': usuario})


# Configurações
@login_required(login_url='/palavra/entrar/')
def configuracoes(request):

    user = request.user
    try:
        user_info = Usuario.objects.get(username=user)
    except Usuario.DoesNotExist:
        user_info = None

    if request.method == 'POST':
        form = UserInfoForm(request.POST, request.FILES, instance=user_info)
        if form.is_valid():
            form.save()
            return redirect('configuracoes')
    else:
        form = UserInfoForm(instance=user_info)

    return render(request, 'palavra/configuracoes.html', {
        'form': form,
        'user_info': user_info
    })


# Features
@login_required(login_url='/palavra/entrar/')
def mostrar_ranking_melhores(request):
    if not request.user.is_authenticated:
        return redirect('/palavra/entrar/')
    jogadores = Usuario.objects.order_by('-pontuacao_total')[:5]
    return render(request, 'palavra/ranking.html', {'top_cinco': jogadores})