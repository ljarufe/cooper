# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *

urlpatterns = patterns('empresa.views',
    url(r'^nosotros/$', 'nosotros', name='nosotros'),
    url(r'^acreditaciones/$', 'acreditaciones', name='acreditaciones'),
    url(r'^practicas/$', 'practicas', name='practicas'),
)
