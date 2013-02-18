var levelcount = 1;
$(document).ready(function() {

	$("#level").load("/level/1/", function() {
		$("#level a.hint").fancybox({
			type : 'ajax'
		});
	});

	$("body").on("click", "#answer", function() {
		$.get("/answer/" + levelcount + "/", {
			guess : $('.guess').val()
		}, function(answer) {
			console.log(answer);
			if (answer) {
				levelcount++;
				$("#level").load("/level/" + levelcount + "/")
			}

		});
	})
});

