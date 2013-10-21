# -*- coding: utf-8 -*-

from django.db import models
from sorl.thumbnail.fields import ImageWithThumbnailsField
from common.widget import ColorPickerWidget
#models
from common.models import Banner


class Categoria(models.Model):
    """
    Supercategoría
    """
    nombre = models.CharField(max_length=50)

    def __unicode__(self):
        return "%s" % self.nombre

    class Meta:
        verbose_name = u"Categoría"
        verbose_name_plural = u"Categorías"


class ColorField(models.CharField):
    """
    Campo para el widget ColorPicker
    """
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 6
        super(ColorField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        kwargs['widget'] = ColorPickerWidget
        return super(ColorField, self).formfield(**kwargs)


class Tipo(models.Model):
    """
    Subcategoria, tiene estilos asociados para la cabecera
    """
    nombre = models.CharField(max_length=50)
    categoria = models.ForeignKey(Categoria, verbose_name=u"Categoría")
    header_bgcolor = ColorField(null=True, blank=True,
                        verbose_name=u"Color de fondo")
    font_color = ColorField(null=True, blank=True,
                    verbose_name=u"Color de fuente")
    break_color = ColorField(null=True, blank=True,
                    verbose_name=u"Color de separaciones")
    header_img = models.ImageField(upload_to="img/tipos", null=True, blank=True, 
                    verbose_name=u"Imágen de fondo")
    banners = models.ManyToManyField(Banner, null=True, blank=True)

    def __unicode__(self):
        return "%s" % self.nombre


class Producto(models.Model):
    """
    Producto
    """
    nombre = models.CharField(max_length=50, db_index=True)
    descripcion = models.TextField(null=True, blank=True, 
                                   verbose_name=u"Descripción")
    imagen = ImageWithThumbnailsField(
                upload_to='img/productos',
                thumbnail={'size': (200, 200)},
                extra_thumbnails={'oferta': {'size': (200, 220), 
                                             'options': ['crop']}},
                generate_on_save=True,
                )
    destacado = models.BooleanField(default=False)
    ESTADO_CHOICES = (
        (u'A', u'Activo'),
        (u'I', u'Inactivo'),
        (u'O', u'Oferta'),
    )
    estado = models.CharField(max_length=1, choices=ESTADO_CHOICES, default='A')
    precio = models.FloatField(blank=True, null=True)
    tipo = models.ForeignKey(Tipo)

    def __unicode__(self):
        return "%s - %s" % (self.nombre, self.descripcion)

    def get_absolute_url(self):
        return "/producto/%i/" % self.id

