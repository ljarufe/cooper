var ofertas = function(urls) {
	var indice = 0;
	var fin = urls.length;
	$('#ofertas img').css('background', 'url('+urls[indice]+')');
	
	$('#sig').click(function() {
		$('#ofertas img').css('background', 'url('+urls[cambiar(1)]+')');
	});
	$('#ant').click(function() {
		$('#ofertas img').css('background', 'url('+urls[cambiar(1)]+')');
	});
	
	function cambiar(num) {
		return indice = (indice+num>=fin)?0:(indice+num<0)?fin-1:indice+num;	//Obtener el indice siguiente o anterior
	}
}
