# models eh o modulo
from django.db import models

# Create your models here.
# Criando a classe Contato que herda da classe Model do modulo models
class Contato(models.Model):
	nome = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	telefone = models.CharField(max_length=14)
	sexo = models.CharField(max_length=1)
	cidade = models.CharField(max_length=50, default="Teresina")

# Aqui eh um metodo pra retornar o nome
	def __str__(self):
		return self.nome