$(function(){
	$('#btnSignUp').click(function(){
		$.ajax({
		    alert('button is clicked.');
			url: '/signUp',
			data: $('form').serialize(),
			type: 'POST',
			success: function(response){
				console.log(response);
			},
			error: function(error){
				console.log(error);
			}
		});
	});
});
