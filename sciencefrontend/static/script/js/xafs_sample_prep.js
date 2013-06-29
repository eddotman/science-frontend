function csrfSafeMethod(method) {
  // these HTTP methods do not require CSRF protection
  return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method)); 
}

$(document).ready(function() {
	$("#inputform").submit(function(event){

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

        var elem = $("#elem").val();
        var ephot = $("#ephot").val();
       	var dens = $("#dens").val();

        var jqxhr = $.post("/xafs_sample_prep/abslen/", {'elem': elem, 'ephot': ephot, 'dens': dens})
        .done(function(data) { 
            $('#result').html("<h3>Total X-ray Absorption Length: " + data + " microns.</h3>"); 
        })
        .fail(function() { 
            $('#result').html('<h3>Something went wrong! Please fix your input and try again.</h3>')
        });
	
    });
});