from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from pathlib import Path
import json
from palavra.models import Usuario, Tema, Palavra

Usuario = get_user_model()

class EntrarViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('entrar')
        self.user = Usuario.objects.create_user(username='testuser', password='testpassword')
    
    def test_entrar_view_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'palavra/login.html')
        self.assertIn('form', response.context)
    
    def test_entrar_view_post_valido(self):
        response = self.client.post(self.url, {
            'username': 'testuser',
            'password': 'testpassword'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('jogo'))
    
    def test_entrar_view_post_invalido(self):
        response = self.client.post(self.url, {
            'username': 'wronguser',
            'password': 'wrongpassword'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'palavra/login.html')
        self.assertIn('form', response.context)
        self.assertFalse(response.context['form'].is_valid())
    
    def test_entrar_view_post_senha_invalida(self):
        response = self.client.post(self.url, {
            'username': 'testuser',
            'password': 'wrongpassword'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'palavra/login.html')
        self.assertIn('form', response.context)
        self.assertFalse(response.context['form'].is_valid())

    def test_entrar_view_post_campos_vazio(self):
        response = self.client.post(self.url, {
            'username': '',
            'password': ''
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'palavra/login.html')
        self.assertIn('form', response.context)
        self.assertFalse(response.context['form'].is_valid())


class CadastrarViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('cadastrar')
    
    def test_cadastrar_view_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'palavra/cadastro.html')
        self.assertIn('form', response.context)
    
    def test_cadastrar_view_post_valido(self):
        response = self.client.post(self.url, {
            'username': 'newuser',
            'password1': 'newpassword123',
            'password2': 'newpassword123',
            'email': 'newuser@example.com'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('jogo'))
    
    def test_cadastrar_view_post_invalido(self):
        response = self.client.post(self.url, {
            'username': '',
            'password1': '',
            'password2': '',
            'email': 'invalidemail'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'palavra/cadastro.html')
        self.assertIn('form', response.context)
        self.assertFalse(response.context['form'].is_valid())


class JogoViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('jogo')
        self.user = Usuario.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

    def test_jogo_view_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'palavra/jogo.html')
        self.assertIn('temas', response.context)
        self.assertIn('usuario', response.context)
    
    def test_jogo_view_post_valido(self):
        session = self.client.session
        session['palavra_correta'] = 'correct'
        session.save()

        tema = Tema.objects.create(descricao='teste')
        Palavra.objects.create(descricao='correct', dificuldade='Fácil', tema=tema)

        response = self.client.post(self.url, json.dumps({'palavra': 'correct'}), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['status'], 'success')
    
    def test_jogo_view_post_invalido(self):
        response = self.client.post(self.url, json.dumps({'palavra': ''}), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()['status'], 'error')


class ConfiguracoesViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('configuracoes')
        self.user = Usuario.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

    def test_configuracoes_view_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'palavra/configuracoes.html')
        self.assertIn('form', response.context)
        self.assertIn('user_info', response.context)
    
    def test_configuracoes_view_post_valido(self):
        caminho_imagem = Path('media/palavra/foto_perfil/admir.jpg')
        with caminho_imagem.open('rb') as imagem:
            imagem_upload = SimpleUploadedFile(imagem.name, imagem.read(), content_type='image/jpeg')
            response = self.client.post(self.url, {
                'username': 'testuser',
                'email': 'testuser@example.com',
                'foto_perfil': imagem_upload
            }, follow=False)

            self.assertIn(response.status_code, [200, 302])

            if response.status_code == 302:
                self.assertRedirects(response, self.url)
            else:
                self.assertEqual(response.status_code, 200)
                self.assertTemplateUsed(response, 'palavra/configuracoes.html')
                self.assertIn('form', response.context)
                self.assertFalse(response.context['form'].errors)

    def test_configuracoes_view_post_invalido(self):
        response = self.client.post(self.url, {
            'username': '',
            'email': 'invalidemail'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'palavra/configuracoes.html')
        self.assertIn('form', response.context)
        self.assertFalse(response.context['form'].is_valid())
