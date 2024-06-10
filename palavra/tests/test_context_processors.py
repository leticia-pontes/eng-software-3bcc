from django.test import TestCase, RequestFactory
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from palavra.context_processors import header_context

class ContextProcessorsTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(username='testuser', password='12345')

    def test_header_context_usuario_autenticado(self):
        self.client.force_login(self.user)

        request = RequestFactory().get('/')
        request.user = self.user

        context = header_context(request)

        self.assertIn('nome', context)
        self.assertIn('foto_perfil', context)
        self.assertIn('pontuacao', context)
        self.assertEqual(context['nome'], self.user.username)
        self.assertEqual(context['foto_perfil'], self.user.foto_perfil)
        self.assertEqual(context['pontuacao'], self.user.pontuacao_total)

    def test_header_context_usuario_nao_autenticado(self):
        request = RequestFactory().get('/')
        request.user = AnonymousUser()

        context = header_context(request)

        self.assertNotIn('nome', context)
        self.assertNotIn('foto_perfil', context)
        self.assertNotIn('pontuacao', context)
