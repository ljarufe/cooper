# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *

urlpatterns = patterns('productos.views',
    url(r'^(?P<categoria>\d+)/(?P<tipo>\d+)/$', 'destacados', name='destacados'),
    url(r'^ofertas/$', 'ofertas', name='ofertas'),
    url(r'^producto/(?P<id>\d+)/$', 'producto', name='producto'),
    
    # json responses
    url(r'^json_fastcooper/(?P<substring>[\w]+)/$', 'json_fastcooper', 
        name='json_fastcooper'),
)
