# -*- coding: utf-8 -*-

'''
Created on 25/08/2010

@author: Mauricio
'''

from django.contrib.syndication.views import Feed
from productos.models import Producto
from django.utils.feedgenerator import Atom1Feed


class UltimasEntradas(Feed):
    title = 'lacooper.com - Laboratorios La Cooper ofertas'
    link = '/ofertas/'
    description = "modificaciones o actualizaciones, novedades y ofertas en lacooper.com"
    author_name = "Laboratorios La Cooper"
    author_email = "sistemas@lacooper.com"

    def items(self):
        producto = Producto.objects.filter(estado='O')
        return producto
