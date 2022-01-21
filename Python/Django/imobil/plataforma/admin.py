from django.contrib import admin

from .models import DiasVisita, Horario, Imovei, Cidade, Imagem, Visitas, Imagens_nossas


@admin.register(Imovei)
class ImoveiAdmin(admin.ModelAdmin):
    list_display = ('rua', 'valor', 'quartos', 'tamanho', 'cidade', 'tipo')  # mostra o que vc quer do model
    list_editable = ('valor', 'tipo') # permite editar os dados do model
    list_filter = ('cidade', 'tipo') # filtra os dados do model


# esse comando registra essas tabelas no admin do django para que nós possamos alteralas a vontade pelo admin
admin.site.register(DiasVisita)
admin.site.register(Horario)
admin.site.register(Imagem)
admin.site.register(Imagens_nossas)
admin.site.register(Cidade)
admin.site.register(Visitas)
