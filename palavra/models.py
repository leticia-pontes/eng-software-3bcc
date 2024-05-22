from django.db import models


## OS COMENTÁRIOS SÃO OS CAMPOS QUE AINDA PRECISAM SER IMPLEMENTADOS

# Senha
class Cadastro(models.Model):
    nome    = models.CharField(max_length=60)
    usuario = models.CharField(max_length=16)
    email   = models.CharField(max_length=40)
    # senha   = models.CharField(max_length=20)
    pontuacao_total = models.IntegerField()

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