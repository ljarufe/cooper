document.domain = document.domain;

function add_message(msg) {
	id = "#" + msg["client"];
    // Hay una conversación con esta persona?
    if($(id).size() == 0) {
        $("#chat-frame").append("<div id='" + msg["client"] + "'><div><h3>" + msg["sender"] + "</h3></div><div class='messages'></div><div class='form'><input type='text' name='message' value='' class='message'><input type='hidden' name='destination' value='" + msg["client"] + "' class='destination'><button class='send'>Enviar</button><div class='clear'></div></div></div>");
    }
    div_destination = "#" + msg["client"] + " .messages";
    $(div_destination).append("<p>" + msg["sender"] + " dijo: " + msg["message"] + "</p>");
    if(!window.isActive) {
    	$.sound.play(url_sound, {track: "track1"});
    }
}

function manager(msg, stomp) {
	switch(msg['code']) {
		// Nuevo request de usuario
		case 1:
			// TODO: Aquí se podría crear el div para la ventana de conversación
			stomp.subscribe("/" + sender + "/" + msg["sender"]);
			break;
		// Nuevo mensaje de usuario
		case 2:
			add_message(msg);
			break;
		default:
			alert("??");
	}
}

function send_message(box) {
	text_box = box.find(".message");
    var message = text_box.val();
    text_box.val("");
    var destination = "/" + sender + "/" + box.find(".destination").val();
    $.post(url_send_message, {"message": message, 
							  "sender": sender, 
							  "destination": destination});
}

$(document).ready(function() {
    // Las alertas se dan sólo cuando la ventana está inactiva
	window.isActive = true;
	$(window).focus(function() { this.isActive = true; });
	$(window).blur(function() { this.isActive = false; });
	
    stomp = new STOMPClient();
    
    stomp.onopen = function(){
		$("#status").html("Conectando...");
    };
    
    stomp.onclose = function(c){
        $("#status").html("Error: " + c);
    };
    
    stomp.onerror = function(error){
        $("#status").html("Error: " + error);
    };
    
    stomp.onerrorframe = function(frame){
        $("#status").html("Error: " + frame);
    };
    
    stomp.onconnectedframe = function() {
    	$("#status").html("Suscribiendo al canal...");
        stomp.subscribe("/" + sender);
        $("#status").html("Conectado");
    };
    
    stomp.onmessageframe = function(frame) {
        manager(JSON.parse(frame.body), stomp);
    };
    
    stomp.connect('localhost', 61613);
    
    // TODO: no funciona
    $(".message").keyup(function(event) {
		var key = event.keyCode;
		if(key == 13) {
			send_message($(this).parent().parent());
		}
	});
    
     $(".send").live('click', function() {
     	send_message($(this).parent());
    });
    
    // Activar o desactivar el sonido
	$("#sonido").click(function(){
		if($.sound.enabled) {
			$.sound.enabled = false;
			$(this).html("Activar sonido");
		}
		else {
			$.sound.enabled = true;
			$(this).html("Desactivar sonido");
		}
	});
});
