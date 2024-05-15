from django.db import models


# Dificuldade
class Palavra(models.Model):
    descricao = models.CharField(max_length=9)

    def __str__(self):
        return self.descricao

# Senha
class Cadastro(models.Model):
    nome    = models.CharField(max_length=60)
    usuario = models.CharField(max_length=16)
    email   = models.CharField(max_length=40)
    # senha   = models.CharField(max_length=20)
    pontuacao_total = models.IntegerField()

    def __str__(self):
        return self.usuario