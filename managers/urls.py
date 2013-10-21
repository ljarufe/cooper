# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *

urlpatterns = patterns('managers.views',
    url(r'^ayuda_clientes$', 'ayuda_clientes', name='ayuda_clientes'),
    url(r'^manager_request$', 'manager_request', name='manager_request'),
    url(r'^send_message$', 'send_message', name='send_message'),
)
