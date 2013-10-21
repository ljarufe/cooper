# -*- coding: utf-8 -*-

from common.utils import direct_response, get_paginated
from django.shortcuts import get_list_or_404
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from common.cache_objects import get_acreditaciones, get_practicas
#models
from empresa.models import Empresa, Acreditacion, Practica


def nosotros(request):
    """
    Información de la empresa
    """
    empresa = get_list_or_404(Empresa)
    return direct_response(request, "empresa/nosotros.html",
                           {"empresa": empresa[0],
                            "titulo": "Nosotros"})
                            

def acreditaciones(request):
    """
    Muestra las acreditaciones de la empresa
    """
    acreditaciones_obj = get_acreditaciones()
    acreditaciones = get_paginated(request, acreditaciones_obj, 2)
    
    return direct_response(request, "empresa/acreditaciones.html",
                           {"acreditaciones": acreditaciones,
                            "titulo": "Acreditaciones"})
                            
                            
def practicas(request):
    """
    Muestra las prácticas de la empresa
    """
    practicas_obj = get_practicas()
    practicas = get_paginated(request, practicas_obj, 2)
        
    return direct_response(request, "empresa/practicas.html",
                           {"practicas": practicas,
                            "titulo": "Prácticas"})

