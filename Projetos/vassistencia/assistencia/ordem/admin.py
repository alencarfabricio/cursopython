from django.contrib import admin
from .models import *


class OrdemAdmin(admin.ModelAdmin):
    model = Ordem
    list_display = ('id','cliente','produto','situacao','codigo_consulta',)

admin.site.register(Marca)
admin.site.register(Produto)
admin.site.register(Modelo)
admin.site.register(Ordem, OrdemAdmin)
