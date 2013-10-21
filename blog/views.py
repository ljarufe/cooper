# -*- coding: utf-8 -*-

from common.utils import direct_response
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from django.http import Http404
from django.db.models import Max
from django.views.decorators.csrf import csrf_exempt
#models
from blog.models import Post, Comentario
# forms
from blog.forms import ComentarioForm


@csrf_exempt
def blog(request, id_post=None):
    """
    Muestra un post con sus comentarios
    """
    # Si se accede a la url sin un id del post se usa el último
    if not id_post:
        id_post = Post.objects.aggregate(Max('id'))
        if id_post['id__max']:
            id_post = id_post['id__max']
        else:
            raise Http404

    post = get_object_or_404(Post, id=id_post)
    comentarios = Comentario.objects.filter(post=post, estado="M")
    comentado = False

    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.post = post
            comentario.save()
            comentado = True
            form = ComentarioForm()
    else:
        form = ComentarioForm()
        
    indice_posts = Post.objects.exclude(id=id_post).order_by('-id')[:10]

    return direct_response(request, "blog/post.html",
                           {"post": post,
                            "comentarios": comentarios,
                            "indice_posts": indice_posts,
                            "form": form,
                            "comentado": comentado,
                            "titulo": "Post: %s" % post.titulo})
                            

def lista_posts(request):
    """
    Muestra la lista de todos los posts ordenados inversamente a su fecha de
    publicación
    """
    indice_posts = Post.objects.all().order_by('-id')
    return direct_response(request, "blog/lista_posts.html",
                           {"indice_posts": indice_posts,
                            "titulo": "Lista de posts"})

