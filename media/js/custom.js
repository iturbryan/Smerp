function load_page(view, target = 'page-wrapper')
		{
		$.ajax({
			  url: 'http://127.0.0.1/accounting/' + view, 
			  type: 'GET', 
			  success: function(response){
			      $('#' + target).fadeOut('slow', function() {
									    $('#' + target).html(response);
									    $('#' + target).fadeIn('slow');
									});
			  }

		      });
		      
		}