from django.db import models

class Ferramenta(models.Model):
    nome = models.CharField(max_length=40)
    descricao = models.TextField()
    tipo = models.CharField(max_length=10)

class Usuario(models.Model):
    ra = models.CharField(max_length=15)