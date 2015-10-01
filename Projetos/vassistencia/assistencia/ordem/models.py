# -*- encoding: utf-8 -*-
# models eh o modulo
from django.db import models
from ..cliente.models import Cliente

# Create your models here.
# Criando a classe Contato que herda da classe Model do modulo models

SITUACAO = (
    ('0', 'em conserto'),
    ('1', 'pronto'),
    ('2', 'aguardando peça'),
)

class TabelaCadastro(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Marca(TabelaCadastro):
    pass

class Modelo(TabelaCadastro):
    pass

class Produto(TabelaCadastro):
    pass

class Ordem(models.Model):
    cliente = models.ForeignKey(Cliente)
    produto = models.ForeignKey(Produto)
    marca = models.ForeignKey(Marca)
    modelo = models.ForeignKey(Modelo)
    situacao = models.CharField(max_length=1, choices=SITUACAO)
    data = models.DateField(auto_now_add=True, editable=False)    
    codigo_consulta = models.CharField(max_length=10, editable=False, default="0000000000")
  
    class Meta:
        verbose_name = "Ordem de servico"
        verbose_name_plural = "Ordens de servico"

    def __str__(self):
        return str(self.id)
    # extend save do django para gerar codigo de consulta
    def save(self, *args, **kwargs):
        import hashlib
        from datetime import datetime
        if not self.id:
            self.codigo_consulta = hashlib.sha1(datetime.now().strftime("%Y%m%d%H%M%S%f").encode('utf-8')).hexdigest()[:10].upper()
        super(Ordem, self).save(*args, **kwargs)
