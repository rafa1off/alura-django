from django.urls import path
from galeria.views import Index, Imagem

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('imagem/', Imagem.as_view(), name='imagem')
]
