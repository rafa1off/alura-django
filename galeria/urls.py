from django.urls import path
from galeria.views import index, Imagem

urlpatterns = [
    path('', index, name='index'),
    path('imagem/', Imagem.as_view(), name='imagem')
]
