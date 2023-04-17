from django.shortcuts import render
from django.views.generic import TemplateView


class Index(TemplateView):
    template_name = 'galeria/index.html'


class Imagem(TemplateView):
    template_name = 'galeria/imagem.html'
