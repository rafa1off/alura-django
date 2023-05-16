from django.contrib import admin
from galeria.models import Fotografias

class ListandoFotografia(admin.ModelAdmin):
    list_display = ('id', 'nome', 'legenda', 'publicada')
    list_display_links = ('nome',)
    search_fields = ('nome', 'legenda')
    list_filter = ('categoria',)
    list_editable = ('publicada',)
    list_per_page = (10)

admin.site.register(Fotografias, ListandoFotografia)
