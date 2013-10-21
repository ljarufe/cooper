# -*- coding: utf-8 -*-

from django.db import models
from productos.models import Tipo
from common.validators import validate_name, validate_phone
    

class Subscripcion(models.Model):
    """
    Modelo para las subscripciones hechas en la página de contacto
    """
    nombre = models.CharField(max_length=100, validators=[validate_name])
    telefono = models.CharField(max_length=15, verbose_name=u'Teléfono',
                                validators=[validate_phone])
    email = models.EmailField(verbose_name=u'e-mail')
    intereses = models.ManyToManyField(Tipo)
    
    def __unicode__(self):
        return u"%s" % self.nombre
        
    class Meta:
        verbose_name = u"Subscripción"
        verbose_name_plural = u"Subscripciones"
