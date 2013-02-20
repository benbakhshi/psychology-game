Game = {

	loadLevel: function(levelNum) {
		$("#level").load("/level/" + levelNum + "/", function() {
	
			// disable all hints except the first
			$("#level .hint:not(:first)").prop('disabled', true);
	
			// clicking a hint displays the hint
			$("#level .hint").each(function(index, el) {
				$(el).fancybox({
					href : $(el).attr("data-url"),
					type : 'ajax'
				});
			});
	
			// enable next hint when clicking on a hint
			$("#level .hint").on("click", function() {
				$(this).next().prop('disabled', false);
			});
	
			// if answer is correct load next level
			$("#answer").on("click", function() {
				$.get("/answer/" + levelNum + "/", {
					guess : $('.guess').val()
				}, function(answer) {
					console.log(answer);
					if (answer) {
						Game.loadLevel(levelNum+1);
					}
				});
			});
		});
	},
	
	//getScore : function() {
		
	//}

}