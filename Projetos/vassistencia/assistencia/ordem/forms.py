from django import forms
from .models import Cliente

class FormBuscaOrdem(forms.Form):
    codigo = forms.CharField(max_length=10, label="", required=False)
