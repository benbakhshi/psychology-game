$(document).ready(function() {

	$("#level").load("/level/1/", function() {
		$("#level a.hint").fancybox({
			type : 'ajax'
		});
	});

	$("body").on("click", "#answer", function() {
		$.get("/answer/1/", {
			guess : $('.guess').val()
		}, function(answer) {
			console.log(answer);
			if () {
				

			} 
		});
	})
}); 