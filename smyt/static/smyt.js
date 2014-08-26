$(document).ready(function(){
	$('.model-link').click(function(){
		
		//$( "#movieList" ).load('/json/' + $(this).attr('href'));
		
		$.getJSON('/json/' + $(this).attr('href'), function(data){
		var html;	
			for (var i = 0; i < data.length; i++){
				html = html + '<tr>';
				for (var j = 0; j < data[i].length; j++){
					html = html + '<td>' + data[i][j] + '</td>';
				}
				html = html + '</tr>';
				}
			$('#item_list').html(html);	

			
		});
		
		return false;
    });
	
});
