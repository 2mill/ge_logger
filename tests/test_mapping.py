from ge import mapping
MOCK_ITEM_INFORMATION = {
	'examine': 'Pudding',
	'id': 4151,
	'name': 'abyssal whip',
	'value': 51515,
	'limit': 8000,
	'members': False,
	'lowalch': 1,
	'highalch': 2,
}

def test_item():
	item = mapping.Item(MOCK_ITEM_INFORMATION)
	assert item.id == MOCK_ITEM_INFORMATION['id']

def test_item_list():
	item_list = mapping.ItemList()
	assert type(item_list.item_list) == list




