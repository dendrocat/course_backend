const post_url = document.location.href + 'api'

const local_rank = $('#local-rank')
const local_level = $('#local-level')
const local_money = $('#local-money')
const local_height = $('#local-height')
const local_width = $('#local-width')

const server_rank = $('#server-rank')
const server_level = $('#server-level')
const server_money = $('#server-money')
const server_height = $('#server-height')
const server_width = $('#server-width')

const play = $('#play')

const error_field = $('#error-field')

const max_money_for_playing = 300
const max_height_for_playing = 700
const max_width_for_playing = 700
const start_paying = 150
const chance_all_money = 0.6

const gate_count = 5
const gate_pay = 150

function random(min = 0, max = 1) {
	return Math.random() * (max - min) + min
}

function clamp(val, min = 0) {
	return Math.max(min, val)
}

function hide_error() {
	error_field.css('opacity', 0)
}

function show_error(msg) {
	error_field.css('opacity', 1)
	error_field.text(msg)
	setTimeout(() => {
		hide_error()
	}, 1000)
}

function earn_money() {
	money = Number(local_money.text())

	if (random() - chance_all_money > 0) {
		dm = max_money_for_playing
	} else dm = Math.round(random() * max_money_for_playing)
	money = money + dm

	local_money.text(money)
}

function change_character() {
	level = Number(local_level.text())
	height = Number(local_height.text())
	width = Number(local_width.text())

	dh = random(-1, 1) * max_height_for_playing
	dw = random(-1, 1) * max_width_for_playing

	height = Math.round(clamp(height + dh))
	width = Math.round(clamp(width + dw))

	if (height + width < gate_count * gate_pay) return false

	mid_height = height - gate_count * gate_pay
	if (mid_height < 0) {
		height = 0
		width += mid_height
	} else height = mid_height

	local_height.text(height)
	local_width.text(width)
	return true
}

function get_changed_data() {
	data = {}
	if (local_level.text() != server_level.text()) {
		data.level = Number(local_level.text())
	}
	if (local_money.text() != server_money.text()) {
		data.money = Number(local_money.text())
	}
	if (local_height.text() != server_height.text()) {
		data.height = Number(local_height.text())
	}
	if (local_width.text() != server_width.text()) {
		data.width = Number(local_width.text())
	}
	return data
}

function getCSRF() {
	let token = 'csrftoken'
	return document.cookie
		.split(';')
		.map(el => el.trim())
		.find(el => el.startsWith(token))
		?.split('=')[1]
}

function patch_on_server() {
	patching_data = get_changed_data()

	$.ajax({
		url: post_url,
		type: 'PATCH',
		data: patching_data,
		headers: {
			'X-CSRFToken': getCSRF(),
		},
		success: function (response) {
			server_level.text(response.level)
			server_money.text(response.money)
			server_height.text(response.height)
			server_width.text(response.width)
		},
		error: function () {
			patch_on_server()
		},
	})
}

$('#play').click(() => {
	hide_error()
	earn_money()
	if (change_character()) {
		local_level.text(Number(local_level.text()) + 1)
	} else {
		play.prop('disabled', true)
		show_error('К сожалению, Вы проиграли.')
		setTimeout(() => play.prop('disabled', false), 1000)
	}
	patch_on_server()
})

function buy(field) {
	val = Number(field.text())
	money = Number(local_money.text())
	level = Number(local_level.text())
	paying = start_paying * (Math.floor(level / 10) + 1)
	if (money < paying) {
		show_error('Недостаточно монет для покупки')
		return 0
	}
	val += paying
	money -= paying
	local_money.text(money)
	field.text(val)
	patch_on_server()
}

$('#width').click(() => {
	buy(local_width)
})

$('#height').click(() => {
	buy(local_height)
})
