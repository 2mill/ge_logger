import exchange
client = exchange.Client()

def test_timeseries():
	item_id = 4151
	interval = '1h'
	items = client.timeseries(
		item_id,
		interval
	)

	assert items.id == 4151



def test_timestamp():
	interval = '1h'
	timestamped_items = client.timestamp(interval)

	assert timestamped_items[0].id == 2

def test_latest():
	item_id = 4151

	item = client.latest(item_id)

	assert item[0].id == 4151





	
