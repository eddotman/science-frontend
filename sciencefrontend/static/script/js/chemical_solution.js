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

        var chem = $("#chem").val();
        var conc = $("#conc").val();
        var vol = $("#vol").val();

        var jqxhr = $.post("/chemical_solutions/compute/", {'chem': chem, 'conc': conc, 'vol': vol})
        .done(function(data) { 
            $('#result').html("<h3>" + data + "</h3>"); 
        })
        .fail(function() { 
            $('#result').html('<h3>Server error! Please try again.</h3>')
        });
	
    });

    $("#clear").click(function(event){
        event.preventDefault();

        document.getElementById('chem').value = "";
        document.getElementById('conc').value = "";
        document.getElementById('vol').value = "";
    });
});