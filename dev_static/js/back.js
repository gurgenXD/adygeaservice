$(document).ready(function(){
    $('#FeedBackForm button').click(function(e) {
        e.preventDefault();
        $(this).prop('disabled', true);

        var csrf_token = $('#FeedBackForm [name="csrfmiddlewaretoken"]').val();
        var recaptcha = $('#FeedBackForm [name="g-recaptcha-response"]').val();
        var name = $('#FeedBackForm input[name="name"]').val();
        var email_or_phone = $('#FeedBackForm input[name="email_or_phone"]').val();
        var text = $('#FeedBackForm textarea[name="text"]').val();

		data = {
            'csrfmiddlewaretoken': csrf_token,
            'g-recaptcha-response': recaptcha,
            email_or_phone: email_or_phone,
            name: name,
            text: text,
        };

		$.ajax({
			type: 'POST',
			url: $('#FeedBackForm').attr('action'),
			data: data,
			success: function(data) {
                if (data.status) {
                    $('#FeedBackBlock .form-success').removeClass('d-none');
                    $('#FeedBackBlock .form-success').addClass('d-flex');
                } else {
                    $('#FeedBackBlock .alert-danger').removeClass('d-none');
                }
            }
		});
    });

    $('#OrderForm button').click(function(e) {
        e.preventDefault();
        $(this).prop('disabled', true);

        var csrf_token = $('#OrderForm [name="csrfmiddlewaretoken"]').val();
        var recaptcha = $('#OrderForm [name="g-recaptcha-response"]').val();
        var name = $('#OrderForm input[name="name"]').val();
        var email_or_phone = $('#OrderForm input[name="email_or_phone"]').val();
        var course_id = $(this).data('course-id');

		data = {
            'csrfmiddlewaretoken': csrf_token,
            'g-recaptcha-response': recaptcha,
            email_or_phone: email_or_phone,
            name: name,
            course_id: course_id,
        };

		$.ajax({
			type: 'POST',
			url: $('#OrderForm').attr('action'),
			data: data,
			success: function(data) {
                if (data.status) {
                    $('#OrderBlock .form-success').removeClass('d-none');
                    $('#OrderBlock .form-success').addClass('d-flex');
                } else {
                    $('#OrderBlock .alert-danger').removeClass('d-none');
                }
            }
		});
    });
});