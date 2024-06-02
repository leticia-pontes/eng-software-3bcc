from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .forms import LoginForm, CadastroForm, UserInfoForm
import json

from .utils import get_palavra_aleatoria
from .models import Palavra, Tema
from .termo import Termo, InvalidAttempt

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

# Lógica do jogo
@login_required(login_url='/palavra/entrar/')
@csrf_exempt
def jogo(request):
    usuario = request.user
    temas = Tema.objects.all()

    # Seleciona a palavra da jogada
    if 'palavra_correta' not in request.session:
        request.session['palavra_correta'] = get_palavra_aleatoria()

    if request.method == 'POST':
        dados = json.loads(request.body)
        palavra = dados.get('palavra', '')
        palavra_correta = request.session['palavra_correta']

        if not palavra:
            return JsonResponse({'status': 'error', 'message': 'No word provided'}, status=400)

        if palavra_correta:
            palavras_validas = Palavra.objects.values_list('descricao', flat=True)
            termo = Termo(palavra_correta, set(palavras_validas))
            try:
                result = termo.test_guess(palavra)
                return JsonResponse({'status': 'success', 'result': result.to_dict()})
            except InvalidAttempt as e:
                return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

    return render(request, 'palavra/jogo.html', {
        'temas': temas, 
        'usuario': usuario,
    })
'''
    Response from backend: 
    Object { status: "error", message: "" }
'''

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