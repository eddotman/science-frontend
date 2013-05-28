$(document).ready(function() {
   	$("#fileform").submit(function(event){
	   	event.preventDefault();
		var jqxhr = $.ajax( "/function_plot/submit/" )
		    .done(function() { $('#result').html("<h2>Form Submitted!</h2>");  })
		    .fail(function() { $('#result').html("<h2>Form Submitted!</h2>"); })
		    .always(function() { $('#result').html("<h2>Form Submitted!</h2>"); });
		});
		return false;
	});
});