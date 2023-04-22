from django.urls import path
from .views import Index, Imagem, buscar

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('imagem/<int:pk>', Imagem.as_view(), name='imagem'),
    path('buscar', buscar, name='buscar')
]
