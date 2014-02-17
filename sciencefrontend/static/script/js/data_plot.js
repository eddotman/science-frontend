
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

       	var dataform = $("#data").val();

        var jqxhr = $.post("/data_plot/plot/", {'data': dataform})
        .done(function(data) { 
            $('#resultWarning').html('')

            $('#result_img').attr("src", data + ".png"); 
            var buttonPDF = '<button class="btn btn-primary" onclick="window.open(\'' + data + '.pdf\', \'_blank\')" >Download PDF version</button>';
            var buttonSVG = '<button class="btn btn-primary" onclick="window.open(\'' + data + '.svg\', \'_blank\')" >Download SVG version</button>';

            $('#resultButtons').html(buttonPDF);
            $('#resultButtons').append(" ");
            $('#resultButtons').append(buttonSVG);
        })
        .fail(function() { 
            $('#result_img').attr("src", null); 
            $('#resultButtons').html('');
            $('#resultWarning').html('<h3>Something went wrong! Please fix your input and try again.</h3>')
        });
	
    });
});