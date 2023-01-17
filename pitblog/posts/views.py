from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from .models import Post, Categoria
from comentarios.models import Comentarios
from django.db.models import Count, Case, When, Q
from comentarios.form import FormComentario
from django.contrib import messages


class PostIndex(ListView):
    '''
    Classes Viwes sobreposição de class original do Django otimiza Retrabalho com Funções
    '''
    model = Post
    template_name = 'posts/index.html'
    context_object_name = 'posts'
    paginate_by = 4


    def get_queryset(self):
        '''
        Função atribuída para trazer a sequencia do último post, ao primeiro assim usuário tem a percepção da entrada por linha de tempo.
        '''
        gs =  super().get_queryset()
        gs = gs.order_by ('-id').filter(publicado=True)
        gs = gs.annotate(
            numero_comentario = Count(
                Case(
                    When (comentarios__publicado_comentario=True, then=1)
                )
            )
        )

        return gs

    def get_context_data(self, **kwargs):
        '''
        Retorno de todas as categorias para utilização dinâmica na views
        '''
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()
        return context

class PostBusca(PostIndex):
    template_name ='posts/post_bus.html'
    
    def get_queryset(self):
        '''
        Sobreposição de função para filtrar de forma precisa, vindo do campo busca, variável “Termo”
        '''
        gs = super().get_queryset()
        termo = self.request.GET.get('termo')

        gs = gs.filter(
            Q(titulo__icontains=termo) | 
            Q(autor__first_name__iexact=termo) |
            Q(categoria__nome_cat__iexact=termo) |
            Q(excerto__icontains=termo)         
        )

        return gs


class PostCategoria(PostIndex):
    template_name = 'posts/post_cat.html'

    def get_queryset(self):
        '''
        Quando clicado a categoria, em exposição será o mesmo desajado pelo Úsuario; nessa função retorna para post_cat.html
        '''
        gs = super().get_queryset()
        categoria = self.kwargs.get('categoria')
        gs = gs.filter(categoria__nome_cat__iexact=categoria)

        return gs


class PostDetalhes(UpdateView):
    template_name = 'posts/post_det.html'
    model = Post
    form_class = FormComentario
    context_object_name =  'post'

    def get_context_data(self, **kwargs):
        '''
        Função responsável para filtrar post, e apresentar detalhes referente ao mesmo.
        '''
        contexto =  super().get_context_data(**kwargs)
        post = self.get_object()
        comentarios = Comentarios.objects.filter(publicado_comentario=True, post_comentario = post.id)
        contexto['comentarios'] = comentarios

        return contexto

    def form_valid(self, form):
        '''
        Formulario pronto fornecido pelo Django assim dentro de form.py em Comentario.
        Assim que implementado somente úsuario autenticado.
        '''
        post = self.get_object()
        comentario = Comentarios(**form.cleaned_data)

        comentario.post_comentario = post

        if self.request.user.is_authenticated:
            comentario.usuario_comentario = self.request.user

        comentario.save()
        messages.success(self.request, 'Comentario enviado')
        return redirect('post_detalhes', pk=post.id)