document.domain = document.domain; 

function manager(msg, stomp) {
	switch(msg['code']) {
		case 1:
			break;
		case 2:
			$("#input_box").append("<p>" + msg["sender"] + ": " + msg["message"] + "</p>");
			if(!window.isActive) {
				$.sound.play(url_sound, {track: "track1"});
			}
			break;
		default:
			alert("??");
	}
};

function send_message() {
    message = $("#message").val();
    $("#message").val("");
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
    
    stomp.onconnectedframe = function(){
    	$("#status").html("Suscribiendo al canal...");
        // Enviar un request al manager
        stomp.subscribe("/" + manager_name);
        $.post(url_manager_request, {"sender": sender, "manager": manager_name});
        // Subscripción al canal exclusivo manager/cliente
        stomp.subscribe(destination);
        $("#status").html("Conectado");
    };
    
    stomp.onmessageframe = function(frame){
        manager(JSON.parse(frame.body), stomp);
    };
    
    stomp.connect('localhost', 61613);
    
    // Enviar un mensaje con el botón o con enter
    $("#message").keyup(function(event) {
		var key = event.keyCode;
		if(key == 13) {
			send_message();
		}
	});

    $("#send").click(function() {
    	send_message();
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
