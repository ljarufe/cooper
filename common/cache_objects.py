# -*- coding: utf-8 -*-

from django.core.cache import cache
#models
from productos.models import Categoria, Tipo
from empresa.models import Acreditacion, Practica
from django.contrib.auth.models import User


def get_menu_productos():
    """
    Devuelve el menu de categorias y tipos en una lista con diccionarios de 
    la forma [{categoria: "categoria1", tipos: ["tipo1", "tipo2"]}]
    """
    menu = cache.get('menu')
    if not menu:
        categorias = Categoria.objects.all()
        menu = []
        for categoria in categorias:
            tipos = Tipo.objects.filter(categoria=categoria)
            item = {"categoria": categoria,
                    "tipos": tipos}
            menu.append(item)
        #cache.set('menu',menu)
    return menu


def get_acreditaciones():
    """
    Obtiene las acreditaciones de cache o hace una consulta
    """
    acreditaciones = cache.get('acreditaciones')
    if not acreditaciones:
        acreditaciones = Acreditacion.objects.all()
        cache.set('acreditaciones', acreditaciones)
    return acreditaciones


def get_practicas():
    """
    Obtiene las practicas de cache o hace una consulta
    """
    practicas = cache.get('practicas')
    if not practicas:
        practicas = Practica.objects.all()
        cache.set('practicas', practicas)
    return practicas
    
    
def get_users(group):
    """
    Devuelve los usuarios de un grupo específico guardados en el caché
    """
    key = 'users_' + group
    users = cache.get(key)
    if not users:
        users = User.objects.filter(groups__name=group)
        cache.set(key, users)
    return users
    
