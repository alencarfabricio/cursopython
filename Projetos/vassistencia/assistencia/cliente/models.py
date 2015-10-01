# models eh o modulo
from django.db import models
from django.utils.safestring import mark_safe

# Create your models here.
# Criando a classe Contato que herda da classe Model do modulo models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    cpf = models.CharField(max_length = 11)
    endereco = models.CharField(max_length = 100)
    bairro   = models.CharField(max_length = 100)
    cidade = models.CharField(max_length = 100) 
    cep = models.CharField(max_length = 100)
    email = models.CharField(max_length=100)
    telefone = models.CharField(max_length=14)
    sexo = models.CharField(max_length=1, choices=(('M','Masculino'),('F','Feminino')))
    cidade = models.CharField(max_length=50, default="Teresina")

    # Aqui eh um metodo pra retornar o nome
    def __str__(self):
        return self.nome


    def ordem(self):
        html = ''
        for ordem in self.ordem_set.exclude(situacao='1'):
            html += '<p><button onclick="window.open(\'/admin/ordem/ordem/{0}/?_popup=1\',\'OS\',\'status=1\')" target>O.S: {1}</button></p>'.format(ordem.id, ordem.id)
        return mark_safe(html)
    ordem.short_description = 'Ordem de serviços em aberto'
    ordem = property(ordem) #nova propriedade para reconhecer no list_display do admin