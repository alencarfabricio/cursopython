from django.http import Http404
from django.shortcuts import render
from .forms import FormBuscaOrdem
from django.template import RequestContext
from .models import Ordem
from django.utils.safestring import mark_safe

# Método usando o paramentro (request)
def VwConsultaOrdem(request):
    if request.method == "POST":
        form = FormBuscaOrdem(request.POST)
        if form.is_valid():
            if Ordem.objects.filter(codigo_consulta = form.cleaned_data['codigo']).exists():
                ordem = Ordem.objects.get(codigo_consulta = form.cleaned_data['codigo']) #objeto da classe Ordem
                resultado=mark_safe('<div class="alert alert-info" role="alert">Olá <b> {0} </b>. A <b>OS: {1}</b> está <b>{2}</b></div>'.format(ordem.cliente, ordem.id, ordem.get_situacao_display()))
            else:
                resultado=mark_safe('<div class="alert alert-danger" role="alert">Código <b>{0}</b> inválido</div>'.format(form.cleaned_data['codigo']))

    else:
        form = FormBuscaOrdem()
        resultado = ''
    # passando dois paramentos (form e resultado)
    return render(request, "busca-ordem.html", {'form':form,'resultado':resultado})

