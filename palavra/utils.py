from .models import Palavra

# Palavra model
def get_palavra_aleatoria():
    if Palavra.objects.exists():
        palavra_aleatoria = Palavra.objects.order_by('?').first()
        return palavra_aleatoria.descricao
    else:
        return None
