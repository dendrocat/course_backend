let get_url = document.location.href.replace('#', '') + 'api'

function set_data(data) {
	$('#local-level').text(data.level)
	$('#local-money').text(data.money)
	$('#local-height').text(data.height)
	$('#local-width').text(data.width)

	$('#server-level').text(data.level)
	$('#server-money').text(data.money)
	$('#server-height').text(data.height)
	$('#server-width').text(data.width)
}

$.get(get_url).done(data => set_data(data))
