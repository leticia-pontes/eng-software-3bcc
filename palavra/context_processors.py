from django.contrib.auth import get_user_model

def header_context(request):
    context = {}
    if request.user.is_authenticated:
        context['nome'] = request.user.username
        context['foto_perfil'] = request.user.foto_perfil
        context['pontuacao'] = request.user.pontuacao_total
    return context
