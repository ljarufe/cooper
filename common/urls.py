# -*- coding: utf-8 -*-

'''
Created on 25/08/2010

@author: Mauricio
'''

from django.conf.urls.defaults import *
from common.rss import UltimasEntradas

site_feeds = {'feed': UltimasEntradas}

urlpatterns = patterns('common.views',
    (r'^feeds/$', UltimasEntradas()),
     url(r'^sitemap/$', 'sitemap' ,name='sitemap'),
)
