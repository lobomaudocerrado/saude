from django.contrib import admin

from registro.models import Pessoa, Meta, Peso

class PessoaAdmin(admin.ModelAdmin):
    list_display  = ['nome', 'apelido', 'login', 'slug']
    search_fields = ['nome', 'apelido', 'login', 'slug']

class MetaAdmin(admin.ModelAdmin):
    list_display  = ['peso', 'data']
    search_fields = ['peso','data']
    list_filter   = ['data']

class PesoAdmin(admin.ModelAdmin):
    list_display  = ['peso', 'data']
    search_fields = ['peso', 'data']
    list_filter   = ['data']





admin.site.register(Pessoa, PessoaAdmin)
admin.site.register(Meta, MetaAdmin)
admin.site.register(Peso, PesoAdmin)
