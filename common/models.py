# -*- coding: utf-8 -*-

from django.db import models
from sorl.thumbnail.fields import ImageWithThumbnailsField
from django.conf import settings


class Banner(models.Model):
    """
    Modelo para banners dinámicos
    """
    nombre = models.CharField(max_length=45, null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True,
                                   verbose_name='Descripcion')
    imagen = ImageWithThumbnailsField(
                upload_to='img/common',
                thumbnail={'size': (800,180),
                           'options': ['upscale', 'max', 'crop']},
                generate_on_save=True,
                null=True,
                blank=True,
                )
    general = models.BooleanField(default=True, 
                help_text=u"Este banner aparecerá en todas las páginas o no")

    def __unicode__(self):
        return '%s' % self.nombre

    def img(self):
        if self.imagen:
            return u'<img src="%s" />' % self.imagen.thumbnail
        else:
            return u'%s sin imagen' % self.nombre

    img.short_description = u'Imagenes'
    img.allow_tags = True
