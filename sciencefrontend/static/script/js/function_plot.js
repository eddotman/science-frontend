$(document).ready(function() {
	$("#funcform").submit(function(event){
   	
   	event.preventDefault();

   	var funct = $("#funct").val();
   	var xmin = $("#xmin").val();
    var xmax = $("#xmax").val();
   	var xincrem = $("#xincrem").val();
   	var url = "/function_plot/" + funct + "/" + xmin + "/" + xmax + "/" + xincrem + "/plot";
   	var url_png = url + ".png";

	$('#result_img').attr("src", url_png);

	var buttonPDF = '<button class="btn btn-primary" onclick="window.open(\'' + url + '.pdf\', \'_blank\')" >Download PDF version</button>';
	var buttonSVG = '<button class="btn btn-primary" onclick="window.open(\'' + url + '.svg\', \'_blank\')" >Download SVG version</button>';

	$('#resultButtons').html(buttonPDF);
	$('#resultButtons').append(" ");
	$('#resultButtons').append(buttonSVG);

	});
});