from django.db import models

# Create your models here.

class contatos(models.Model):
	nome = models.CharField(max_length=100)
	endereco = models.CharField(max_length=100)
	cidade = models.CharField(max_length=50)
	estado = models.CharField(max_length=2)
	cep = models.CharField(max_length=10)
	telefone = models.CharField(max_length=14)
	email = models.CharField(max_length=100)

	def __str__(self):
		return self.nome


	