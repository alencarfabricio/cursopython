from django import forms

from .models import Contato

class ContatoForm(forms.ModelForm):
	class Meta:
		model = Contato
		fields = ('nome', 'endereco', 'cidade', 'estado', 'cep', 'telefone', 'email')