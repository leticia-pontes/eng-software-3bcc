import uuid
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from palavra.forms import CadastroForm, LoginForm, UserInfoForm
from palavra.models import Usuario

class CadastroFormTest(TestCase):

    def test_cadastro_form_valido(self):
        form = CadastroForm(data={
            'username': 'newuser',
            'password1': 'newpassword123',
            'password2': 'newpassword123',
            'email': 'newuser@example.com'
        })
        self.assertTrue(form.is_valid())

    def test_cadastro_form_invalido(self):
        form = CadastroForm(data={})
        self.assertFalse(form.is_valid())

class LoginFormTest(TestCase):

    def setUp(self):
        self.user = Usuario.objects.create_user(
            username='testuser',
            password='password',
            email='testuser@example.com'
        )

    def test_login_formulario_valido(self):
        form = LoginForm(data={'username': 'testuser', 'password': 'password'})
        self.assertTrue(form.is_valid())

    def test_login_formulario_invalido(self):
        form = LoginForm(data={})
        self.assertFalse(form.is_valid())

class UserInfoFormTest(TestCase):

    def setUp(self):
        self.user = Usuario.objects.create_user(
            username='testuser',
            password='password',
            email='testuser@example.com'
        )
        self.user_info = {
            'username': f'newusername_{uuid.uuid4().hex[:6]}',
            'email': 'newemail@example.com',
            'foto_perfil': SimpleUploadedFile(
                "test_image.jpg",
                b"file_content",
                content_type="image/jpeg"
            )
        }

    def test_userinfo_form_valido(self):
        form = UserInfoForm(
            data=self.user_info,
            files={'foto_perfil': self.user_info['foto_perfil']},
            instance=self.user
        )
        self.assertTrue(form.is_valid())

    def test_userinfo_form_invalido(self):
        form = UserInfoForm(data={}, instance=self.user)
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors)

    def test_userinfo_form_field_attributes(self):
        form = UserInfoForm()
        self.assertEqual(form.fields['foto_perfil'].widget.attrs['accept'], 'image/*')
        self.assertEqual(form.fields['foto_perfil'].widget.attrs['class'], 'form-control-file')

    def test_userinfo_form_com_arquivo(self):
        form = UserInfoForm(
            data=self.user_info,
            files={'foto_perfil': self.user_info['foto_perfil']},
            instance=self.user
        )
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['foto_perfil'], self.user_info['foto_perfil'])
