from unittest.mock import patch, MagicMock
from django.test import TestCase
from palavra.models import Palavra, Tema
from palavra.utils import get_palavra_aleatoria

class UtilsTest(TestCase):

    def setUp(self):
        tema = Tema.objects.create(descricao='Geral')
        Palavra.objects.create(descricao='choro', dificuldade=Palavra.FACIL, tema=tema)
        Palavra.objects.create(descricao='anjos', dificuldade=Palavra.MEDIO, tema=tema)
        Palavra.objects.create(descricao='renda', dificuldade=Palavra.DIFICIL, tema=tema)

    def test_get_palavra_aleatoria(self):
        palavra_aleatoria = get_palavra_aleatoria()
        palavras_existentes = Palavra.objects.values_list('descricao', flat=True)
        self.assertIn(palavra_aleatoria, palavras_existentes)

    @patch('palavra.utils.Palavra.objects.exists', MagicMock(return_value=False))
    def test_get_palavra_aleatoria_banco_vazio(self):
        palavra_aleatoria = get_palavra_aleatoria()
        self.assertIsNone(palavra_aleatoria)