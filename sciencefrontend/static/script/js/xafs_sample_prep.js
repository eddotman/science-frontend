function csrfSafeMethod(method) {
  // these HTTP methods do not require CSRF protection
  return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method)); 
}

$(document).ready(function() {
	function submit(){

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
        var ephot = $("#ephot").val();
        var dens = $("#dens").val();
       	var bn = $("#bn").val();

        var jqxhr = $.post("/xafs_sample_prep/abslen/", {'chem': chem, 'ephot': ephot, 'dens': dens, 'bn': bn})
        .done(function(data) { 
            $('#result').html("<h3>" + data + "</h3>"); 
        })
        .fail(function() { 
            $('#result').html('<h3>Server error! Please try again.</h3>')
        });
	
    });

    function clear_fields(){
        document.getElementById('chem').value = "";
        document.getElementById('ephot').value = "";
        document.getElementById('dens').value = "";
        document.getElementById('bn').value = "";
    });
});