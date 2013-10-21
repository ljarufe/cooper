# -*- coding: utf-8 -*-

'''
Created on 20/08/2010

@author: Mauricio
'''

from django import forms
from common.widget import Markitup
from productos.models import Producto


class ProductoForm(forms.ModelForm):
    """
    Formulario para agregar un banner
    """
    descripcion = forms.CharField(widget=Markitup())
    
    class Meta:
        model = Producto
