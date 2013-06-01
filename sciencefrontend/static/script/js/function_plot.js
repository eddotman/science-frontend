$(document).ready(function() {
	$("#funcform").submit(function(event){
   	
   	event.preventDefault();

   	var funct = $("#funct").val();
   	var xmin = $("#xmin").val();
    var xmax = $("#xmax").val();
   	var xincrem = $("#xincrem").val();
   	var url = "/function_plot/" + funct + "/" + xmin + "/" + xmax + "/" + xincrem + "/plot";
   	var url_png = url + ".png";
   	//var url = "/function_plot/cos(x)/1/5/1/plot.png";

	$('#result_img').attr("src", url_png);

	var buttonPDF = '<button class="btn btn-primary" onclick="location.href=\'' + url + '.pdf\'" >Download PDF version</button>';
	var buttonSVG = '<button class="btn btn-primary" onclick="location.href=\'' + url + '.svg\'" >Download SVG version</button>';

	$('#resultButtons').html(buttonPDF);
	$('#resultButtons').append(" ");
	$('#resultButtons').append(buttonSVG);

	});
});