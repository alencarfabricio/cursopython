from django.shortcuts import render

from .forms import ContatoForm

# Create your views here.

def contato(request):
	if request.method == 'POST':
		form = ContatoForm(request.POST)
		if form.is_valid():
			form.save()
			return render(request, 'sucesso.html')
		else:
			print(form.errors)
	else:
		form = ContatoForm()
	return render(request, 'contato.html', {'form': form})