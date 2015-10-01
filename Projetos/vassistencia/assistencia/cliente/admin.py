from django.contrib import admin
from .models import Cliente
from ..ordem.models import Ordem

# Register your models here.

#@admin.register(Contato)
class ClienteAdmin(admin.ModelAdmin):
    #Colunas que vai ser aparecer no site
    list_display = ('nome', 'email', 'telefone','sexo','cidade', 'ordem',)
    # lupa de pesquisa
    search_fields = ('nome', 'email','sexo')

# Registrando o admin para ter acesso pelo admin
admin.site.register(Cliente, ClienteAdmin)
