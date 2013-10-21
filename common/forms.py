# -*- coding: utf-8 -*-

from django import forms
from common.widget import Markitup
from common.models import Banner


class StandartForm(forms.Form):
    """
    An standart form with error class
    """
    error_css_class = 'error'
    required_css_class = 'required'


class BannerForm(forms.ModelForm):
    """
    Formulario para agregar un banner
    """
    descripcion = forms.CharField(widget=Markitup())
    
    class Meta:
        model = Banner
        

class LoginForm(forms.Form):
    """
    Formulario de logeo
    """
    username = forms.CharField(label="Usuario")
    password = forms.CharField(widget=forms.PasswordInput)
