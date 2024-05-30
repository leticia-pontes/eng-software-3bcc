def usuario(request):
    nome = None
    if request.user.is_authenticated:
        nome = request.user.nome
    return {'nome': nome}

def pontuacao(request):
    pontuacao = None
    if request.user.is_authenticated:
        pontuacao = request.user.pontuacao_total
    return {'pontuacao': pontuacao}