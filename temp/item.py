import sys
sys.path.append("../")
from datetime import date
import datetime
from osrsbox import items_api
import ge
ITEM_DATA = {
	'id': 2611,
	'name': "Abyssal Whip",
	'pricing': {
		'high': {
			'price': 555,
			'time': datetime.datetime(2021,12,12, 18, 2)
		},
		'low': {
			'price': 554,
			'time': datetime.datetime(2021, 12,12, 18, 3)
			# 'time': date.today() - 1
		},
	}
}
def get_none_id() -> bool:
	item_list = items_api.load()
	# tools.get_id(item_list, 5000000)
	assert(None, ge.tools.get_id(item_list, "5000000"))