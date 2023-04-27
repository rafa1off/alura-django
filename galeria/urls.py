from django.urls import path
from .views import Index, Imagem, Buscar

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('imagem/<int:foto_id>', Imagem.as_view(), name='imagem'),
    path('buscar', Buscar.as_view(), name='buscar')
]
