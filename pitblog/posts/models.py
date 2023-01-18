from django.db import models
from categorias.models import Categoria
from django.contrib.auth.models import User
from django.utils import timezone

class Post(models.Model):

    titulo = models.CharField(max_length=150, verbose_name='Titulo')
    autor = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank= True, null=True, verbose_name='Autor')
    data = models.DateTimeField(default=timezone.now)
    conteudo = models.TextField(verbose_name='Conteudo')
    excerto = models.TextField(verbose_name='Introdução')
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING, blank=True, null=True)
    imagem = models.ImageField(upload_to='img_post/%Y/%m', blank=True, null=True)
    publicado = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo