function csrfSafeMethod(method) {
  // these HTTP methods do not require CSRF protection
  return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method)); 
}

$(document).ready(function() {
	$("#submit").click(function(event){

        event.preventDefault();

        var csrftoken = $.cookie('csrftoken');

        $.ajaxSetup({
            crossDomain: false, // obviates need for sameOrigin test
            beforeSend: function(xhr, settings) {
                if (!csrfSafeMethod(settings.type)) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            }
        });

        var outfile = $("#outfile").val();
        var radius = $("#radius").val();
        var crystal = $("#crystal").val();
	
    });

    $("#clear").click(function(event){
        event.preventDefault();

        document.getElementById('outfile').value = "";
        document.getElementById('radius').value = "";
        document.getElementById('crystal').value = "";
    });
});