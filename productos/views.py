# -*- coding: utf-8 -*-

from common.utils import direct_response, json_response
from django.shortcuts import get_object_or_404
# models
from productos.models import Producto, Categoria, Tipo


def destacados(request, categoria, tipo):
    """
    Muestra los productos destacados de cada tipo
    """
    # TODO: Establecer algún orden para enviar los productos?
    productos = Producto.objects.filter(tipo__id=tipo).exclude(estado="I")
    categoria_obj = get_object_or_404(Categoria, id=categoria)
    tipo_obj = get_object_or_404(Tipo, id=tipo)
    banners = tipo_obj.banners.all()
    return direct_response(request,"productos/destacados.html",
                           {"productos": productos,
                            "categoria": categoria_obj.nombre,
                            "tipo": tipo_obj,
                            "banners": banners,
                            "titulo": "Productos %s de %s" % (categoria_obj.nombre, tipo_obj.nombre)})


def ofertas(request):
    """
    muestra todas las ofertas para los feeds
    """
    productos = Producto.objects.filter(estado="O")
    return direct_response(request,"productos/ofertas.html",
                           {"productos": productos,
                            "titulo": "Ofertas Laboratorios La cooper"})


def producto(request, id):
    """
    Muestra uno de los productos en oferta en una tabla según su id
    """
    producto = Producto.objects.get(id=id)
    return direct_response(request, "productos/oferta_unitaria.html",
                           {"productos": producto,
                            "titulo": "Oferta Laboratorios La cooper"})


def json_fastcooper(request, substring):
    """
    Búsqueda de una subcadena en la tabla productos
    """
    match_products = Producto.objects.filter(nombre__istartswith=substring)
    productos = []
    for match_producto in match_products:
        producto = {'id': match_producto.id,
                    'nombre': match_producto.nombre,
                    'descripcion': match_producto.descripcion,
                    'imagen': u"%s" % match_producto.imagen.thumbnail,}
        productos.append(producto)
    
    return json_response(productos)

