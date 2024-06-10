from django.test import TestCase
from palavra.models import Usuario
from django.core.files.uploadedfile import SimpleUploadedFile
import os

class UsuarioModelTest(TestCase):

    def test_create_usuario(self):
        user = Usuario.objects.create_user(username='testuser', email='test@test.com', password='password', foto_perfil='fotos/admir.jpg')
        self.assertEqual(user.username, 'testuser')

    def test_foto_perfil_field(self):
        current_directory = os.path.dirname(os.path.abspath(__file__))
        
        media_directory = os.path.join(current_directory, 'fotos/')
        
        photo_path = os.path.join(media_directory, 'fotoleticia.jpg')

        self.assertTrue(os.path.isfile(photo_path))

        with open(photo_path, 'rb') as file:
            photo = SimpleUploadedFile('fotoleticia.jpg', file.read(), content_type='image/jpeg')
        
        user = Usuario.objects.create_user(username='testuser', password='password', foto_perfil=photo)
        self.assertTrue(user.foto_perfil)
        
        nova_foto_path = os.path.join(media_directory, 'admir.jpg')
        with open(nova_foto_path, 'rb') as file:
            nova_foto = SimpleUploadedFile('admir.jpg', file.read(), content_type='image/jpeg')
        
        user.foto_perfil = nova_foto
        user.save()
        
        self.assertTrue(os.path.isfile(user.foto_perfil.path))
