from django.contrib import admin

from .models import contatos

# Register your models here.

class ContatoAdmin(admin.ModelAdmin):
	pass

admin.site.register(contatos, ContatoAdmin)