# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *

urlpatterns = patterns('clientes.views',
    url(r'^contactanos/$', 'contacto', name='contacto'),
    url(r'^subscripcion/$', 'subscripcion', name='subscripcion'),
    url(r'^cerrar_sesion$', 'cerrar_sesion', name='cerrar_sesion'),
    url(r'^recuperar_password$', 'recuperar_password', 
        name='recuperar_password'),
    url(r'^recuperar_password/(?P<usuario>[\w]+)/(?P<password>[\w]+)/$',
        'recuperar_password', name='recuperar_password'),
    url(r'^ayuda_en_linea/(?P<manager>[\w]+)/$', 'ayuda_en_linea',
        name='ayuda_en_linea')
)
