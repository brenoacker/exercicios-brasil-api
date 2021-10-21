from django.contrib import admin
from exercicios.models import DDD, SiglaEstado, Regiao

class DDDs(admin.ModelAdmin):
    list_display = ('ddd', 'id')
    list_display_links = ('ddd',)
    search_fields = ('ddd',)
    list_per_page = 20

admin.site.register(DDD, DDDs)

class SiglaEstados(admin.ModelAdmin):
    list_display = ('sigla', 'id')
    list_display_links = ('sigla',)
    search_fields = ('sigla',)
    list_per_page = 20

admin.site.register(SiglaEstado, SiglaEstados)

class Regioes(admin.ModelAdmin):
    list_display = ('A', 'B', 'C', 'id')
    list_display_links = ('A', 'B', 'C',)
    search_fields = ('A', 'B', 'C',)
    list_per_page = 20

admin.site.register(Regiao, Regioes)