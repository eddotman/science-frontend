
function csrfSafeMethod(method) {
  // these HTTP methods do not require CSRF protection
  return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method)); 
}

$(document).ready(function() {
	$("#dataform").submit(function(event){

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

    var jqxhr = $.post("/data_plot/plot.png", {'data': dataform})
    .done(function(data) { $('#result_img').attr("src", data); })
    .fail(function() { alert("fail"); });

	});
});