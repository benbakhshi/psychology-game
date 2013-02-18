$(document).ready(function() {

<<<<<<< HEAD
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
=======
	/* This is basic - uses default settings */
	
	$("a.hint").fancybox({type: 'ajax'})
	
	
	
});
>>>>>>> de2be314ef356ce85b944916093292209bcfaab1
