from datetime import date
ITEM_DATA = {
	'id': 2611,
	'name': "Abyssal Whip",
	'pricing': {
		'high': {
			'price': 555,
			'time': date.today()
		},
		'low': {
			'price': 554,
			'time': date.today() - 1
		}
	}
}