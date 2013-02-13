jQuery(document).ready(function() {


    function loadContent(riddle) {

        $('.question').text(riddle.question);

        $.each(riddle.hints, function(){

            for (var i=0; i < riddle.hints.length; i++) {

                var hint = $("<a/>").html(riddle.hints[i]).addClass('btn btn-large btn-success').data('toggle','popover').data('content','"+riddle.hints[i]+"').data('original-title','Hint "+i+"')

                $('#hints').append(hint)
                }
            })
        console.log(riddle);
        console.log(riddle.hints);
        console.log(riddle.hints[0]);
        console.log(riddle.possible_answers);
            }

    // loadContent(RIDDLE);
	$.get('/get_a_question/', function(j) {
		loadContent(j);
	});


//    $('#hints').after(
//        '<a href="#" id="hint" class="btn btn-large btn-success" data-toggle="popover" title="" data-content="Hint 1 Content" data-original-title="Hint 1 Title">Hint 1</a>'
//    )

//    $('#hint').click( function() {
//        $(this).addClass('disabled'),
//        $(this).popover('show')
//    }).mouseleave( function() {
//            $('#hint').popover('hide')
//        })
//
//    $('body').on('mouseenter','#hint.disabled', function() {
//        $(this).popover('show');
//        }).mouseleave( function(){
//            $(this).parent('#hint').popover('hide');
//        });



//
//
//    function take_new_q() {
//		$("#loader").load("./question");
//		number++
//		$('div div.number').text(number);
//
//	}
//
//	function check_q(question,answer) {
//		$.get("./answer", {q:question,a:answer}, function(res){
//			if (res == "True") {
//				take_new_q();
//
//				if (score == 0) {score += 1000}
//
//				else {
//					score = score * 2
//					}
//				console.log(score)
//				$('div div.score').text(score);
//			}
//			else {
//				quit_game();
//
//			}
//		})
//	}
//
//	$("div#loader").on('click', 'button.opt', function() {
//		var q = $('div.question').data('q');
//		var a = $(this).data('opt')
//		if (q != null && a != undefined) {
//			$("ul.options button").attr('disabled','disabled');
//			check_q(q,a);
//		}
//	});
});
