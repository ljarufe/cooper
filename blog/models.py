# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.db import models
from datetime import datetime
from common.validators import validate_name


class Post(models.Model):
    """
    Post para el blog
    """
    titulo = models.CharField(max_length=200, verbose_name=u"Título")
    texto = models.TextField()
    fecha = models.DateField()
    usuario = models.ForeignKey(User)

    def __unicode__(self):
        return u"%s por %s en %s" % (self.titulo, self.usuario, self.fecha)
        
    class Meta:
        ordering = ['-fecha']


class Comentario(models.Model):
    """
    Comentario para un post
    """
    nombre = models.CharField(max_length=50, validators=[validate_name])
    email = models.EmailField(verbose_name=u"e-mail")
    # TODO: se puede hacer un validador para el campo de los comentarios
    comentario = models.TextField()
    fecha = models.DateField(default=datetime.now)
    post = models.ForeignKey(Post)
    ESTADO_CHOICES = (
        (u"M", u"Moderado"),
        (u"E", u"Espera"),
    )
    estado = models.CharField(max_length=1, choices=ESTADO_CHOICES, default="E")

    def __unicode__(self):
        return u"%s comentado por %s" % (self.post, self.nombre)

