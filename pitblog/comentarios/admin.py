from django.contrib import admin
from .models import Comentarios

class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_comentario', 'email_comentario', 'data_comentario', 'publicado_comentario' ,)
    list_display_links = ('id', 'nome_comentario', 'data_comentario',)
    list_editable = ('publicado_comentario',)

admin.site.register(Comentarios, ComentarioAdmin)