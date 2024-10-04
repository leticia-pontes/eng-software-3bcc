from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.apps import apps
from palavra.models import Tema, Palavra, Usuario

class UsuarioModelTest(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        apps.get_app_config('palavra')

    def setUp(self):
        self.usuario = Usuario(username='testuser', password='testpass', pontuacao_total=100)
        self.usuario.save()

    def test_str(self):
        self.assertEqual(str(self.usuario), 'testuser')

    def test_foto_perfil(self):

        image = SimpleUploadedFile(
            name='admir.jpg',
            content=b'fake image content',
            content_type='image/jpeg'
        )
        
        self.usuario.foto_perfil.save('admir.jpg', image)

        self.assertIsNotNone(self.usuario.foto_perfil)
        self.assertTrue(self.usuario.foto_perfil.name.startswith('palavra/foto_perfil/admir'))


class TemaModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        apps.get_app_config('palavra')

    def setUp(self):
        self.tema = Tema.objects.create(descricao='Teste')

    def test_str(self):
        self.assertEqual(str(self.tema), 'Teste')


class PalavraModelTest(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        apps.get_app_config('palavra')

    def setUp(self):
        self.tema = Tema.objects.create(descricao='Teste')
        self.palavra = Palavra.objects.create(descricao='palavra', dificuldade=Palavra.FACIL, tema=self.tema)

    def test_str(self):
        self.assertEqual(str(self.palavra), 'palavra')

    def test_dificuldade_choices(self):
        self.assertEqual(self.palavra.dificuldade, Palavra.FACIL)
        self.assertIn(self.palavra.dificuldade, dict(Palavra.DIFICULDADE_CHOICES).keys())
