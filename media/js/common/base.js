
function mostrar_busqueda(id) {
    url = "/productos/producto/" + id;
    // Esto tiene que cargarse en la misma página :@
	window.location.href = url;
};

function popUp(URL) {
	day = new Date();
	id = day.getTime();
	eval("page" + id + " = window.open(URL, '" + id + "', 'toolbar=0,scrollbars=0,location=,statusbar=0,menubar=0,resizable=0,width=300,height=450,top=100,left=50');");
}

/* Inicio de Sesion  */
var inicio_sesion = function() {
	$('#inicio_sesion').css('left',$('#user').offset().left);
};

var hola = function() {
	inicio_sesion();
	$('#user').addClass('user_activo');
	$('#inicio_sesion').fadeIn(100);
};

var user = function() {
	
	$('#li_inicio_sesion').hover(function() {
		inicio_sesion();
		$('#user').addClass('user_activo');
		$('#inicio_sesion').fadeIn(100);
	}, function() {
		inicio_sesion();
		$('#user').removeClass();
		$('#inicio_sesion').fadeOut(100);
	});
};


$(window).resize(function() {
  inicio_sesion();
});
