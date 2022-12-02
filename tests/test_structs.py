from pyWikiGE.structs import *

def test_latest_item():
	item = LatestItem(
		4151,
		5,
		6,
		10,
		10
	)
	assert str(item) == r"{'id': 4151, 'high': 5, 'low': 6, 'high_time': 10, 'low_time': 10}"

def test_item_price_interval():
	item = ItemPriceInterval(
		5,
		5,
		5,
		5,
		5
	)
	assert str(item) == r"{'timestamp': 5, 'avg_high_price': 5, 'avg_low_price': 5, 'high_price_volume': 5, 'low_price_volume': 5}"

def test_timed_item():
	price_point = [
		ItemPriceInterval(
			5,
			5,
			5,
			5,
			5
		)
	]
	item = TimedItem(
		'4151', price_point
	)
	assert str(item) == r"{'id': '4151', 'price_points': [{'timestamp': 5, 'avg_high_price': 5, 'avg_low_price': 5, 'high_price_volume': 5, 'low_price_volume': 5}]}"

def test_mapped_item():
	item = MappedItem(
		4151,
		'aby whip',
		5,
		'something',
		True,
		5,
		5,
		5,
		'icon.png'
	)
	assert str(item) == r"{'id': 4151, 'name': 'aby whip', 'value': 5, 'members': 'something', 'low_alch': True, 'high_alch': 5, 'limit': 5, 'examine': 5, 'icon': 'icon.png'}"