$(document).ready(function() {
	$("#fileform").submit(function(event){
   	event.preventDefault();
	var jqxhr = $.ajax( "/function_plot/plot.png" )
	    .done(function(data) { $('#result_img').attr("src", "data:image/png;base64," + data);  })
	    .fail(function() { $('#result').html("<h2>Failed!</h2>");  });
	});



	return false;
});