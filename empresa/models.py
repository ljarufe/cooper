# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from common.validators import validate_phone
from sorl.thumbnail.fields import ImageWithThumbnailsField
from django.db.models import Max
from django.core.cache import cache
from django.conf import settings


class Empresa(models.Model):
    """
    Datos dinámicos para La Cooper
    """
    nombre = models.CharField(max_length=90)
    direccion = models.CharField(max_length=90, null=True, blank=True,
                                 verbose_name='direccion')
    telefono = models.CharField(max_length=15, null=True, blank=True,
                                verbose_name='teléfono',
                                validators=[validate_phone])
    email = models.EmailField(verbose_name='e-mail')
    historia = models.TextField()
    mision = models.TextField(verbose_name=u"Misión")
    vision = models.TextField(verbose_name=u"Visión")
    valores = models.TextField()

    def __unicode__(self):
        return '%s' % self.nombre

    def save(self, *args, **kwargs):
        """
        Si se crea una nueva empresa la anterior desaparecerá
        """
        old_id = Empresa.objects.aggregate(Max('id'))
        try:
            empresa = Empresa.objects.get(id=old_id['id__max'])
            empresa.delete()
        except Empresa.DoesNotExist:
            pass
        cache.set('cache_empresa', self)
        return super(Empresa, self).save(*args, **kwargs)


class Acreditacion(models.Model):
    """
    Acreditación de la empresa
    """
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField(verbose_name=u"Descripción")
    imagen = ImageWithThumbnailsField(
                upload_to='img/empresa',
                thumbnail={'size': (100, 100), 'options': ['autocrop']},
                generate_on_save=True,
                null=True,
                blank=True,
                )

    def __unicode__(self):
        return '%s' % self.nombre

    class Meta:
        verbose_name = u"Acreditación"
        verbose_name_plural = u"Acreditaciones"

    def img(self):
        if self.imagen:
            return u'<img src="%s%s" width="250"/>' % (settings.MEDIA_URL, self.imagen)
        else:
            return u'%s sin imagen' % self.nombre

    img.short_description = u'Imágenes'
    img.allow_tags = True


class Practica(models.Model):
    """
    Prácticas de la empresa
    """
    titulo = models.CharField(max_length=50, verbose_name=u"Título")
    descripcion = models.TextField(verbose_name=u"Descripción")
    imagen = ImageWithThumbnailsField(
                upload_to='img/empresa',
                thumbnail={'size': (200, 150), 'options': ['autocrop']},
                generate_on_save=True,
                null=True,
                blank=True,
                )

    def __unicode__(self):
        return '%s' % self.titulo

    class Meta:
        verbose_name = u"Práctica"
        verbose_name_plural = u"Prácticas"

    def img(self):
        if self.imagen:
            return u'<img src="%s%s" width="250"/>' % (settings.MEDIA_URL, self.imagen)
        else:
            return u'%s sin imagen' % self.titulo

    img.short_description = u'Imágenes'
    img.allow_tags = True

