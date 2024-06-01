from django.contrib.auth import get_user_model

def header_context(request):
    nome = None
    foto_perfil = None
    pontuacao = None
    if request.user.is_authenticated:
        nome = request.user.username
        foto_perfil = request.user.foto_perfil
        pontuacao = request.user.pontuacao_total
    return {'nome': nome, 'foto_perfil': foto_perfil, 'pontuacao': pontuacao}
