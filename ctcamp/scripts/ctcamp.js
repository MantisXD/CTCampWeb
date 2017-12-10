
function simpleTemplating(data) {
    var html = '<table class = "table table-hover table-striped">';
    html += '<thead><tr><th>TITLE</th>';
    html += '<th>MANAGER</th>';
    html += '<th>CONFERENCE</th>';
    html += '</tr></thead>';
    html += '<tbody>';
    $.each(data, function(index, item){
        html += '<tr contentID=' + item['id'] + ' conference=' + item['conference'] +'>';
        html += '<td>' + item['title'] +'</td>';
        html += '<td>' + item['manager'] +'</td>';
        html += '<td>' + item['conference'] +'</td>';
        html += '</tr>';
    });
    html += '</tbody></table>';
    return html;
}

$('#pagination-container').pagination({
    dataSource: g_contentsList[0]["contents"],
    className: 'paginationjs-theme-blue',
    ulClassName: 'pagination justify-content-center',
    callback: function(data, pagination) {
        // template method of yourself
        var html = simpleTemplating(data);
        $('#data-container').html(html);
    }
});

$("tr[contentID]").click(function(){
	var contentID = $(this).attr("contentID");
	console.log(contentID);
	var conference = $(this).attr("conference");
	
	var url = "/" + conference + "/contents/" + contentID + ".html";
	location.href = url;
});


$('#v-pills-tab a').on('click', function (e) {
  e.preventDefault()
  $(this).tab('show')
});
