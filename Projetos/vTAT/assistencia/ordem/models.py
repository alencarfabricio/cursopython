from django.db import models

# Create your models here.

class Ordem (models.Model):

	ordem_id = models.AutoField(primary_key=True)
	ordem_produto = models.CharField(max_length=45)
	ordem_qtpeca = models.CharField(max_length=45)
	ordem_peca = models.CharField(max_length=11)
	ordem_pedido = models.CharField(max_length=45)
	ordem_dtpedido = models.CharField(max_length=45)
	ordem_situacao = models.CharField(max_length=45)
	ordem_codsenha = models.CharField(max_length=45)
	ordem_dataordem = models.DateTimeField(auto_now_add=True)
	