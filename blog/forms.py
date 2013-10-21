# -*- coding: utf-8 -*-

'''
Created on 18/08/2010

@author: Mauricio
'''

from django import forms
from common.widget import Markitup
from blog.models import Post, Comentario
from django.contrib.auth.models import User


class PostForm(forms.ModelForm):
    """
    Formulario para ingresar Entradas al blog
    """
    texto = forms.CharField(widget=Markitup)
    # Seleccionar que tipo de usuarios pueden hacer un post
#    lista_usuarios = User.objects.filter(is_staff=True)
#    usuarios = ((usuario.id, usuario.username) for usuario in lista_usuarios)
#    usuario = forms.ChoiceField(widget=forms.RadioSelect(), choices=usuarios)
    
    class Meta:
        model = Post


class ComentarioAdminForm(forms.ModelForm):
    """
    Formulario para la edición de comentarios en el Administrador de contenidos
    """
    comentario = forms.CharField(widget=Markitup())
    
    class Meta:
        model = Comentario
        

class ComentarioForm(forms.ModelForm):
    """
    Formulario para la subida de comentarios por los usuarios
    """
    comentario = forms.CharField(widget=Markitup())
    
    class Meta:
        model = Comentario
        fields = ("nombre", "email", "comentario")

