from django.conf.urls import include, url
urlpatterns = [
    url(r'^$', 'assistencia.ordem.views.VwConsultaOrdem'),
]
