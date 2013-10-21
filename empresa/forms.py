# -*- coding: utf-8 -*-

'''
Created on 18/08/2010

@author: Mauricio
'''

import django.forms as forms
from common.widget import Markitup
from empresa.models import Empresa, Acreditacion, Practica


class EmpresaForm(forms.ModelForm):
    """
    Formulario para el modelo Empresa
    """
    historia = forms.CharField(widget=Markitup())
    mision = forms.CharField(widget=Markitup())
    vision = forms.CharField(widget=Markitup())
    valores = forms.CharField(widget=Markitup())
    
    class Meta:
        model = Empresa


class AcreditacionForm(forms.ModelForm):
    """
    Formulario para el modelo Acreditación
    """
    descripcion = forms.CharField(widget=Markitup())
    
    class Meta:
        model = Acreditacion


class PracticaForm(forms.ModelForm):
    """
    Formulario para el modelo Practica
    """
    descripcion = forms.CharField(widget=Markitup())
    
    class Meta:
        model = Practica

