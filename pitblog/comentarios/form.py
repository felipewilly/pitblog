from django.forms import ModelForm
from .models import Comentarios


class FormComentario(ModelForm):
    def clean(self):
        data = self.cleaned_data
        nome = data.get('nome_comentario')
        email = data.get('email_comentario')
        comentario = data.get('comentario')

        if len(nome) < 3:
            self.add_error(
                'nome_comentario',
                'Nome precisar ter mais que 3 caractere')


    class Meta:
        model = Comentarios
        fields = ('nome_comentario', 'email_comentario', 'comentario')