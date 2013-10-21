# -*- coding: utf-8 -*-

import django.forms as forms
from common.validators import validate_user, validate_name
from django.core.validators import validate_email
# models
from clientes.models import Subscripcion
from productos.models import Tipo


class SubscripcionForm(forms.ModelForm):
    """
    Formulario para el contacto con un cliente
    """
    intereses = forms.ModelMultipleChoiceField(
                    widget=forms.CheckboxSelectMultiple(),
                    queryset=Tipo.objects.all()
                )
    class Meta:
        model = Subscripcion
        fields = ('nombre', 'telefono', 'email', 'intereses')


class ContactoForm(forms.Form):
    """
    Formulario de contacto
    """
    nombres = forms.CharField(validators=[validate_name])
    email = forms.CharField(validators=[validate_email])
    asunto = forms.CharField()
    consulta = forms.CharField(widget=forms.Textarea)
    

class RecuperarForm(forms.Form):
    """
    Formulario para recuperar contraseña
    """
    usuario = forms.CharField(validators=[validate_user])
