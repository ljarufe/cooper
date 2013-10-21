# -*- coding: utf-8 -*-

from django import template
from django.core.cache import cache
from django.shortcuts import get_object_or_404
from common.cache_objects import get_menu_productos, get_users
from django.conf import settings
# models
from productos.models import Categoria, Tipo, Producto
from common.models import Banner
from empresa.models import Empresa

register = template.Library()

@register.inclusion_tag('common/templatetags/menu_categorias.html')
def get_menu_categorias():
    """
    Muestra el menu de categorías y sus tipos para el widget SpryAssert
    """
    return {'menu': get_menu_productos()}


@register.inclusion_tag('common/templatetags/cache_ofertas.html')
def get_ofertas():
    """
    Muestra las ofertas
    """
    ofertas = cache.get('ofertas')
    if not ofertas:
        ofertas = Producto.objects.filter(estado="O")
        cache.set('ofertas',ofertas)

    return {'ofertas': ofertas,
            'MEDIA_URL': settings.MEDIA_URL}


@register.inclusion_tag('common/templatetags/banners.html')
def get_banners():
    """
    todos los banners para ser cargados en el template base
    """
    banners = cache.get('banners')
    if not banners:
        banners = Banner.objects.filter(general=True)
        cache.set('banners', banners)
    return {'banners': banners}
    
    
@register.inclusion_tag('common/templatetags/managers_list.html')
def get_managers():
    """
    Devuelve una lista de managers disponibles desde el cache
    """
    return {'managers': get_users('managers')}
    

