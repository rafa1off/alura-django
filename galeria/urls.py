from django.urls import path
from .views import index, Imagem, buscar

urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:pk>', Imagem.as_view(), name='imagem'),
    path('buscar', buscar, name='buscar')
]
