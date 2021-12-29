from datetime import date
from osrsbox import items_api
import struct
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
			# 'time': date.today() - 1
		}
	}
}
# def get_none_id() -> bool:
# 	item_list = items_api.load()
# 	# tools.get_id(item_list, 5000000)
# 	assert(None, tools.get_id(item_list, "5000000"))