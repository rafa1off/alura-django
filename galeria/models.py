from django.db import models
from datetime import datetime


class Fotografias(models.Model):

    categorias = [
        ('Nebulosa', 'Nebulosa'),
        ('Galáxia', 'Galáxia'),
        ('Estrela', 'Estrela'),
        ('Planeta', 'Planeta')
    ]

    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    categoria = models.CharField(max_length=100, choices=categorias, default='')
    descricao = models.TextField(null=False, blank=False)
    foto = models.ImageField(upload_to='fotos/%Y/%m/%d/', blank=True)
    publicada = models.BooleanField(default=False)
    data = models.DateTimeField(default=datetime.now, blank=False)

    def __str__(self):
        return f'Fotografia {self.nome}'
