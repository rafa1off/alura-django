from django.urls import path
from .views import Login, Cadastro

urlpatterns = [
    path('login', Login.as_view(), name='login'),
    path('cadastro', Cadastro.as_view(), name='cadastro'),
]
