from django.contrib import admin
from core.models import Evento


# Register your models here.
class EventoAdmin(admin.ModelAdmin):  # essa classe adminitra coisa do banco, aqui estou colocando para sempre
    # aparecer o titulo, a data e a data que foi criado o evento no nome dele
    list_display = ('id', 'titulo', 'data_evento', 'data_criacao')
    list_filter = ('usuario', 'data_evento')


admin.site.register(Evento, EventoAdmin)  # registrando a tabela no admin do django
# associa as classes a aba admin do django, sendo que as duas passadas precisam ter coisas em comum
# pois uma registra a outra
