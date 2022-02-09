from ge import structs

def test_valid_id():
	item_list: object = structs.ItemList()
	item = item_list.find(4151)
	assert item.name.lower() == "abyssal whip"
def test_valid_id_given_str_id():
	item_list: object = structs.ItemList()
	identifier = '4151'
	item = item_list.find(int(identifier))
	assert item.name.lower() == "abyssal whip"
def test_valid_name():
	item_list: object = structs.ItemList()
	item = item_list.find("abyssal whip")
	assert item is not None

def test_pricing():
	mock_data = {
		'high': {
			'price': 500,
			'time': 11111
		},
		'low': {
			'price': 400,
			'time': 1110
		}
	}
	price_obj = structs.Pricing(mock_data)
	assert price_obj.high_price == 500