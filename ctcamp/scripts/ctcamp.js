window.onload = function(){
	function simpleTemplating(data) {
	    var html = '<table class = "table table-hover table-striped">';
	    html += '<thead><tr><th>TITLE</th>';
	    html += '<th>PRESENTER</th>';
	    html += '<th>CONFERENCE</th>';
	    html += '</tr></thead>';
	    html += '<tbody>';
	    $.each(data, function(index, item){
	        html += '<tr contentID=' + item['id'] + '>';
	        html += '<td>' + item['title'] +'</td>';
	        html += '<td>' + item['presenter'] +'</td>';
	        html += '<td>' + item['conference'] +'</td>';
	        html += '</tr>';
	    });
	    html += '</tbody></table>';
	    return html;
	}

    $('#pagination-container').pagination({
	    dataSource: g_contentsList[0]["contents"],
	    //className: ,
	    ulClassName: "pagination",
	    callback: function(data, pagination) {
	        // template method of yourself
	        var html = simpleTemplating(data);
	        $('#data-container').html(html);
	    }
	});

	$("tr[contentID]").click(function(){
		var contentID = $(this).attr("contentID");
		console.log(contentID);
		var conference = contentID.split("_")[0];
		
		var url = "/" + conference + "/contents/" + contentID + ".html";
		location.href = url;
	});

}

$('#v-pills-tab a').on('click', function (e) {
  e.preventDefault()
  $(this).tab('show')
});


3