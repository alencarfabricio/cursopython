from django.db import models

# Create your models here.

class Clientes(models.Model):

	clientes_id = models.AutoField(primary_key=True)
	clientes_nome = models.CharField(max_length=45)
	clientes_sobrenome = models.CharField(max_length=45)
	clientes_cpf = models.CharField(max_length=11)
	clientes_endereco = models.CharField(max_length=45)
	clientes_bairro = models.CharField(max_length=45)
	clientes_cep = models.CharField(max_length=8)
	clientes_cidade = models.CharField(max_length=45)
	clientes_telefone = models.CharField(u'Celular', max_length=14, help_text='(99)99999-9999')
	clientes_data_cadastro = models.DateTimeField(auto_now_add=True)
	clientes_email = models.CharField(max_length=45)
