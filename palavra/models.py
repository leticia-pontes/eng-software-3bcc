from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    pontuacao_total = models.IntegerField(default=0)
    foto_perfil = models.ImageField(upload_to='palavra/foto_perfil/', null=True, blank=True)

    def __str__(self):
        return self.username
        
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