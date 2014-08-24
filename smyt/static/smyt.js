$(document).ready(function(){
	$('.model-link').click(function(){
		
		//$( "#movieList" ).load('/json/' + $(this).attr('href'));
		
		$.getJSON('/json/' + $(this).attr('href'), function(data){
		var html;	
			for (var i = 0; i < data['rows'].length; i++	 ){
				html = html + data['rows'][i]['name'];
				}
			$('#item_list').html(html);	

			
		});
		
		return false;
    });
	
});
