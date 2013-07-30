$(document).ready(function() {
	$(function () {
        $('#file').fileupload({
            dataType: 'html',
            always: function (e, data) {
                $('#result').html('<a href="' + data.result + '" ><h1>Download Formatted File</h1></a>');
            }

        });
    });
});
