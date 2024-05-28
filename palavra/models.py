from django.db import models
from django.contrib.auth.hashers import make_password, check_password


## OS COMENTÁRIOS SÃO OS CAMPOS QUE AINDA PRECISAM SER IMPLEMENTADOS

# Senha
class Cadastro(models.Model):
    nome    = models.CharField(max_length=60)
    usuario = models.CharField(max_length=16)
    email   = models.CharField(max_length=40)
    senha   = models.CharField(max_length=30)
    pontuacao_total = models.IntegerField()

    def set_senha(self, senha_crua):
        self.senha = make_password(senha_crua)

    def verificar_senha(self, senha_crua):
        return check_password(senha_crua, self.senha)

    def __str__(self):
        return self.usuario
        
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