from .models import Palavra

# Palavra Model
def get_palavra_aleatoria():
    palavra_aleatoria = Palavra.objects.order_by('?').first()
    return palavra_aleatoria.descricao if palavra_aleatoria else None