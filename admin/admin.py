# -*- coding: utf-8 -*-

from django.contrib import admin
# models
from blog.models import *
from common.models import *
from clientes.models import *
from empresa.models import *
from productos.models import *
# forms
from common.forms import BannerForm
from empresa.forms import EmpresaForm, AcreditacionForm, PracticaForm
from blog.forms import PostForm, ComentarioAdminForm
from productos.forms import ProductoForm
from clientes.forms import SubscripcionForm


class AdminEmpresa(admin.ModelAdmin):
    form = EmpresaForm


class AdminAcreditacion(admin.ModelAdmin):
    form = AcreditacionForm
    list_display = ('nombre', 'descripcion', 'img')


class AdminPractica(admin.ModelAdmin):
    form = PracticaForm
    list_display = ('titulo', 'descripcion', 'img')


class AdminBanner(admin.ModelAdmin):
    form = BannerForm
    list_display = ('nombre', 'descripcion', 'img')


class AdminPost(admin.ModelAdmin):
    form = PostForm
    list_display = ('titulo', 'usuario', 'fecha')
    

class AdminComentario(admin.ModelAdmin):
    form = ComentarioAdminForm
    list_display = ('post', 'nombre', 'estado')


class AdminProducto(admin.ModelAdmin):
    form = ProductoForm
    list_display = ('nombre', 'tipo', 'estado', 'destacado')
    
    
class AdminSubscripcion(admin.ModelAdmin):
    form = SubscripcionForm
    list_display = ('nombre', 'email')

#common
admin.site.register(Banner, AdminBanner)
# blogs
admin.site.register(Post, AdminPost)
admin.site.register(Comentario, AdminComentario)
# clientes
admin.site.register(Subscripcion, AdminSubscripcion)
# empresa
admin.site.register(Empresa, AdminEmpresa)
admin.site.register(Acreditacion, AdminAcreditacion)
admin.site.register(Practica, AdminPractica)
# productos
admin.site.register(Categoria)
admin.site.register(Tipo)
admin.site.register(Producto, AdminProducto)

