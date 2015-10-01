from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    model = Cliente
