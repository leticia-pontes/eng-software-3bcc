from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json

from .utils import get_palavra_aleatoria
from .models import Palavra, Tema, Usuario
from .forms import LoginForm, CadastroForm, UserInfoForm
from .termo import Termo, InvalidAttempt

# Página Inicial
def index(request):
    return render(request, 'palavra/index.html')

# Autenticação
def entrar(request):
    error_message = None
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
            error_message = form.error_messages['invalid_login']
    else:
        form = LoginForm(request)
    return render(request, 'palavra/login.html', {'form': form, 'error': error_message})


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
@login_required
def jogo(request):
    usuario = request.user
    temas = Tema.objects.all()

    if 'palavra_correta' not in request.session or request.session.get('nova_palavra', False):
        request.session['palavra_correta'] = get_palavra_aleatoria()
        request.session['nova_palavra'] = False

    if request.method == 'POST':
        try:
            dados = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status=400)

        palavra = dados.get('palavra', '')
        palavra_correta = request.session['palavra_correta']

        if not palavra:
            return JsonResponse({'status': 'error', 'message': 'No word provided'}, status=400)

        if palavra_correta:
            palavras_validas = Palavra.objects.values_list('descricao', flat=True)
            termo = Termo(palavra_correta, set(palavras_validas))
            try:
                result = termo.test_guess(palavra)
                if result.win:
                    usuario.pontuacao_total += 10
                    usuario.save()

                    request.session['nova_palavra'] = True
                    return JsonResponse({'status': 'success', 'result': result.to_dict(), 'nova_pontuacao': usuario.pontuacao_total})
            except InvalidAttempt as e:
                return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

    return render(request, 'palavra/jogo.html', {
        'temas': temas, 
        'usuario': usuario,
    })


@login_required
def get_pontuacao(request):
    if request.user.is_authenticated:
        pontuacao = request.user.pontuacao_total
        return JsonResponse({'pontuacao': pontuacao})
    else:
        return JsonResponse({'error': 'Usuário não autenticado'}, status=401)

# Configurações
@login_required(login_url='/palavra/entrar/')
def configuracoes(request):
    user_info = request.user
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

# @login_required
# def excluir_conta(request):
#     if request.method == 'POST':
#         request.user.delete()
#         messages.success(request, 'Sua conta foi excluída com sucesso.')
#         return redirect('index')
#     return render(request, 'palavra/excluir_conta.html')

# Features
@login_required(login_url='/palavra/entrar/')
def mostrar_ranking_melhores(request):
    if not request.user.is_authenticated:
        return redirect('/palavra/entrar/')
    jogadores = Usuario.objects.order_by('-pontuacao_total')[:5]
    return render(request, 'palavra/ranking.html', {'top_cinco': jogadores})
