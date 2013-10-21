# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *

urlpatterns = patterns('blog.views',
    url(r'^(?P<id_post>\d+)/$', 'blog', name='blog'),
    url(r'^$', 'blog', name='blog'),
    url(r'^lista_posts$', 'lista_posts', name='lista_posts'),
)
