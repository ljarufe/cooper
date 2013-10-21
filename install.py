# -*- coding: utf-8 -*-

"""
Este archivo debe ser ejecutado despues de crear los modelos, crea los grupos 
y sus permisos para clientes y los encargados de área.

>> python manage.py syncdb
>> python install.py
"""

from os import environ
environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from settings import *
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

# Crear lso permisos
user = ContentType.objects.get(model='User')

cliente_perm = Permission(name=u'Puede entrar a algún canal de chat de ayuda',
                          codename='puede_ayuda', 
                          content_type=user)
cliente_perm.save()

manager_perm = Permission(name=u'Puede administrar un canal de chat', 
                          codename='puede_chat',
                          content_type=user)
manager_perm.save()

# Crear los grupos iniciales
clientes = Group(name='clientes')
clientes.save()
clientes.permissions.add(cliente_perm)
clientes.save()

managers = Group(name='managers')
managers.save()
managers.permissions.add(manager_perm)
managers.save()

