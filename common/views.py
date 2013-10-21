# -*- coding: utf-8 -*-

from common.utils import direct_response
from common.cache_objects import get_menu_productos
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
#models
from productos.models import Producto
from empresa.models import Acreditacion, Practica


@csrf_exempt
def inicio(request):
    """
    Muestra 3 productos destacados al azar
    """
    usuario_invalido = False
    productos = Producto.objects.filter(destacado=True).order_by("?")[:3]
        
    if request.method == 'POST':
        nombre = request.POST['usuario']
        password = request.POST['password']
        usuario = authenticate(username=nombre, password=password)
        if usuario is not None:                    
            if usuario.is_active:
                login(request, usuario)
            else:
                return direct_response(request, "common/inicio.html",
                           {"productos": productos,
                            "usuario_invalido": usuario_invalido,
                            "titulo": "Inicio"})
        else:
            usuario_invalido = True
    #Prueba de error 500
    #x = Producto.objects.get(Id=8000)
    return direct_response(request, "common/inicio.html",
                           {"productos": productos,
                            "usuario_invalido": usuario_invalido,
                            "titulo": "Inicio"})
                            
                            
def sitemap(request):
    """
    Índice del mapa del sitio
    """
    acreditaciones = Acreditacion.objects.all()
    practicas = Practica.objects.all()
    return direct_response(request, "common/sitemap.html",
                           {"acreditaciones": acreditaciones,
                            "practicas": practicas,
                            "menu": get_menu_productos(),
                            "titulo": "Mapa del sitio"})

