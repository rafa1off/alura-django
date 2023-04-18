from django.shortcuts import render
from django.views.generic import TemplateView


def index(request):
    dados = {
        1: {'nome': 'Nebulosa de Carina',
            'legenda': 'webbtelescope.org / NASA / James Webb'},
        2: {'nome': 'Galáxia NGC 1079',
            'legenda': 'nasa.org / NASA / Hubble'}
    }
    return render(request, 'galeria/index.html', {'cards': dados})


class Imagem(TemplateView):
    template_name = 'galeria/imagem.html'
