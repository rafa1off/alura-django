from django.db import models


class Fotografias(models.Model):

    categorias = [
        ('NEBULOSA', 'Nebulosa'),
        ('GALÁXIA', 'Galáxia'),
        ('ESTRELA', 'Estrela'),
        ('PLANETA', 'Planeta')
    ]

    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    categoria = models.CharField(max_length=100, choices=categorias, default='')
    descricao = models.TextField(null=False, blank=False)
    foto = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return f'Fotografia {self.nome}'
