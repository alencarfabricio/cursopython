from django.contrib import admin

from .models import Contato

# Register your models here.

#@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
	#Colunas que vai ser aparecer no site
	list_display = ('nome', 'email', 'telefone','sexo','cidade')
	# lupa de pesquisa
	search_fields = ('nome', 'email','sexo')
	pass

# Registrando o admin para ter acesso pelo admin
admin.site.register(Contato, ContatoAdmin)
