from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class UsuarioManager(BaseUserManager):
    def create_user(self, email, nome, senha=None):
        if not email:
            raise ValueError('O E-mail é obrigatório!')
        if not nome:
            raise ValueError('O Nome é obrigatório!')

        email = self.normalize_email(email)
        user = self.model(email=email, nome=nome)
        user.set_password(senha)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nome, senha=None):
        user = self.create_user(email, nome, senha)
        user.is_active = True
        user.is_admin = True
        user.save(using=self._db)
        return user

class Usuario(AbstractBaseUser, PermissionsMixin):
    nome = models.CharField(max_length=60, unique=True)
    email = models.EmailField(max_length=40, unique=True)
    senha = models.CharField(max_length=25)
    pontuacao_total = models.IntegerField(default=0)
    foto_perfil = models.ImageField(upload_to='foto_perfil/')
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UsuarioManager()

    USERNAME_FIELD = 'nome'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.nome

    @property
    def is_staff(self):
        return self.is_admin

    @property
    def is_superuser(self):
        return self.is_admin
        
class Tema(models.Model):
    descricao = models.CharField(max_length=20)

    def __str__(self):
        return self.descricao

class Palavra(models.Model):
    FACIL = 'Fácil'
    MEDIO = 'Médio'
    DIFICIL = 'Difícil'
    
    DIFICULDADE_CHOICES = [
        (FACIL, 'Fácil'),
        (MEDIO, 'Médio'),
        (DIFICIL, 'Difícil'),
    ]

    descricao = models.CharField(max_length=9)
    dificuldade = models.CharField(max_length=10, choices=DIFICULDADE_CHOICES)
    tema = models.ForeignKey(Tema, on_delete=models.CASCADE)

    def __str__(self):
        return self.descricao