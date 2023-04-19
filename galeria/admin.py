from django.contrib import admin
from .models import Fotografias

class ListandoFotografia(admin.ModelAdmin):
    list_display = ('id', 'nome', 'legenda')
    list_display_links = ('id', 'nome')
    search_fields = ('nome', 'legenda')

admin.site.register(Fotografias, ListandoFotografia)
