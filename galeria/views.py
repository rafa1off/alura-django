from django.shortcuts import render, get_object_or_404
from django.views import View
from galeria.models import Fotografias


class Index(View):
    def get(self, request):
        fotografias = Fotografias.objects.order_by('data').filter(publicada=True)
        return render(request, 'galeria/index.html', {'cards': fotografias})


'''def index(request):
    fotografias = Fotografias.objects.order_by('data').filter(publicada=True)
    return render(request, 'galeria/index.html', {'cards': fotografias})'''


class Imagem(View):
    def get(self, request, foto_id):
        fotografia = get_object_or_404(Fotografias, pk=foto_id)
        return render(request, 'galeria/imagem.html', {'fotografia': fotografia})

'''def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografias, pk=foto_id)
    return render(request, 'galeria/imagem.html', {'fotografia': fotografia})'''

class Buscar(View):
    def get(self, request):
        fotografias = Fotografias.objects.order_by('data').filter(publicada=True)

        if 'buscar' in request.GET:
            nome_a_buscar = request.GET['buscar']
            if nome_a_buscar:
                fotografias = fotografias.filter(nome__icontains=nome_a_buscar)

        return render(request, 'galeria/buscar.html', {'cards': fotografias})

'''def buscar(request):
    fotografias = Fotografias.objects.order_by('data').filter(publicada=True)

    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)

    return render(request, 'galeria/buscar.html', {'cards': fotografias})'''
