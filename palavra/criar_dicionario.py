import os
import sys
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "termooo.settings")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

django.setup()

from palavra.models import Palavra, Tema

default_tema, _ = Tema.objects.get_or_create(descricao='Geral')

caminho = BASE_DIR + '/palavra/'

with open(caminho + 'palavras.txt', 'r', encoding='utf-8') as palavras_file:
    for palavra in palavras_file:
        palavra_limpa = palavra.strip()

        if not Palavra.objects.filter(descricao=palavra_limpa).exists():
            p = Palavra()
            p.descricao = palavra_limpa
            p.tema_id = default_tema.id
            p.save()
            print(f'Palavra adicionada: {palavra_limpa}')

all_palavras = Palavra.objects.all()
for palavra in all_palavras:
    print(palavra.descricao)
