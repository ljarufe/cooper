# -*- coding: utf-8 -*-

from common.utils import direct_response
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse
import stomp
import json

conn = stomp.Connection()
conn.start()
conn.connect()

@permission_required('auth.puede_chat')
def ayuda_clientes(request):
    """
    Ayuda a clientes, el manager esta subscrito a un canal con su nombre de 
    usuario donde recibirá requests de los clientes
    """
    conn.subscribe(destination="/%s" % request.user.username, ack="auto")
    # TODO: Cambiar el puerto y hostname
    return direct_response(request, 'managers/ayuda_cliente.html',
                           {'port': 9000, 
                            'hostname': "127.0.0.1"})
                            
                            
def manager_request(request):
    """
    Un cliente necesita ayuda del encargado
    """
    cliente = request.POST.get("sender", "")
    manager = request.POST.get("manager", "")
    msg = {
        "code": 1,
        "sender": cliente,
    }
    json_msg = json.dumps(msg)
    conn.send(json_msg, destination="/%s" % manager)
    
    # TODO: si esta suscrito ya, no hay que suscribirlo de nuevo
    conn.subscribe(destination="/%s/%s" % (manager, cliente), ack='auto')

    return HttpResponse("ok")
    
    
def send_message(request):
    """
    Envío de un mensaje
    """
    destination = request.POST.get("destination", "")
    msg = {
        "code": 2,
        "sender": request.POST.get("sender", ""),
        "message": request.POST.get("message", ""),
        "client": destination.split("/")[2],
    }
    json_msg = json.dumps(msg)
    conn.send(json_msg, destination=destination)

    return HttpResponse("ok")

