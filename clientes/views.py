# -*- coding: utf-8 -*-

from common.utils import direct_response, send_html_mail, make_password
from django.shortcuts import get_object_or_404, get_list_or_404
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
# forms
from clientes.forms import SubscripcionForm, ContactoForm, RecuperarForm
# models
from empresa.models import Empresa


@csrf_protect
def subscripcion(request):
    """
    Muestra y procesa el formulario de suscripción, además de información de la 
    empresa más detallada
    """
    if request.method == 'POST':
        form = SubscripcionForm(request.POST)
        if form.is_valid():
            form.save()
            # e-mail hacia el cliente
            subject = u"Contacto con La Cooper"
            data = (
                form.cleaned_data['nombre'],
            )
            # TODO: Cambiar el destinatario
            send_html_mail(subject,"suscripcion_cliente.html",data,
                           "luis.jarufe@hotmail.com",
                           [form.cleaned_data["email"]])
            # e-mail hacia el administrador
            subject = u"Contacto con el Sr.(a) %s" % form.cleaned_data['nombre']
            intereses = ""
            for interes in form.cleaned_data['intereses']:
            	 intereses += "<li>%s</li>" % interes
            data = (
                form.cleaned_data['nombre'],
                form.cleaned_data['telefono'],
                form.cleaned_data['email'],
				intereses,
            )
            # TODO: Cambiar el remitente y destinatario del correo
            send_html_mail(subject,"suscripcion_cooper.html",data,
                           "luis.jarufe@hotmail.com",
                           ["luis.jarufe@hotmail.com"])
			
			# TODO: Puede ser necesaria una página de "correo enviado"
            return HttpResponseRedirect(reverse('inicio'))
    else:
        form = SubscripcionForm()

    empresa = get_list_or_404(Empresa)

    return direct_response(request,"empresa/suscripcion.html",
                           {"empresa": empresa[0],
                            "form": form,
                            "titulo": u"Suscripción"})


@csrf_exempt
def contacto(request):
    """
    Muestra el formualrio para la sección de contactos
    """
    if request.method == "POST":
        form = ContactoForm(request.POST)
        if form.is_valid():
            # e-mail hacia el cliente
            subject = u"Contacto con La Cooper"
            data = (
                form.cleaned_data['nombres'],
            )
            # TODO: Cambiar el remitente del correo
            send_html_mail(subject, "contacto_cliente.html", data,
                           "luis.jarufe@hotmail.com",
                           [form.cleaned_data["email"]])

            # e-mail hacia el administrador
            subject = u"Contacto con el Sr.(a) %s" % form.cleaned_data['nombres']
            data = (
                form.cleaned_data['nombres'],
                form.cleaned_data['email'],
                form.cleaned_data['asunto'],
                form.cleaned_data['consulta'],
            )
            # Cambiar el remitente y destinatario del correo
            send_html_mail(subject, "contacto_cooper.html", data,
                           "luis.jarufe@hotmail.com",
                           ["luis.jarufe@hotmail.com"])
                           
			# TODO: Puede ser necesaria una página de "correo enviado"
            return HttpResponseRedirect(reverse('inicio'))
    else:
        form = ContactoForm()

	# TODO: Debería seguir funcionando sin necesidad de ingresar una empresa
    empresa = get_list_or_404(Empresa)
    return direct_response(request, "empresa/contactanos.html", 
                           {"empresa": empresa[0],
                            "form": form,
                            "titulo": "Contactanos"})


def cerrar_sesion(request):
    """
    logout de cliente
    """
    logout(request)
    return HttpResponseRedirect(reverse('inicio'))
    
    
@csrf_exempt
def recuperar_password(request, usuario=None, password=None):
	"""
	Recuperar una cuenta mediante el envío de un nuevo password
	"""
	# Enviar un e-mail con una nueva contraseña - aún no se cambia
	if request.method == 'POST':
		form = RecuperarForm(request.POST)
		if form.is_valid():
			cliente = User.objects.get(username=form.cleaned_data['usuario'])
			password = make_password(6)
			subject = u"Recuperar mi contraseña en La Cooper"
			data = (
				password,
				form.cleaned_data['usuario'],
				password,
			)
			# TODO: cambiar el email remitente
			no_email = False
			if cliente.email:
				send_html_mail(subject, "recuperar_password.html", data,
							   "luis.jarufe@hotmail.com",
							   [cliente.email])
			else:
				no_email = True

			return direct_response(request, 'clientes/confirmacion.html',
								   {'no_email': no_email,
								    'titulo': 'Confirmación'})
	else:
		form = RecuperarForm()

	# Cambiar la contraseña al confirmar el e-mail
	if usuario and password:
		cliente = User.objects.get(username=usuario)
		cliente.set_password(password)
		cliente.save()
		return HttpResponseRedirect(reverse('inicio'))

	# Mostrar el formulario de solicitud
	return direct_response(request, 'clientes/recuperar_password.html',
						   {'form': form,
						   'titulo': 'Recuperar Contraseña'})


@permission_required('auth.puede_ayuda')
def ayuda_en_linea(request, manager):
	"""
	Ingresar al área de chat con alguno de los managers de área
	"""
	manager_obj = get_object_or_404(User, username=manager)
	# TODO: Cambiar el hostname
	return direct_response(request, 'clientes/ayuda_en_linea.html',
						   {'port': 9000,
						    'hostname': "127.0.0.1",
						    'manager': manager_obj})

