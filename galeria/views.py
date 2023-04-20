from django.shortcuts import render, get_object_or_404
from galeria.models import Fotografias


def index(request):
    fotografias = Fotografias.objects.order_by('data').filter(publicada=True)
    return render(request, 'galeria/index.html', {'cards': fotografias})


def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografias, pk=foto_id)
    return render(request, 'galeria/imagem.html', {'fotografia': fotografia})
