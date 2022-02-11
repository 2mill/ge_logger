import ge.structs as structs
import json


# Not trying to accidentally DDOS the wiki here.
mapping_data = json.load(open('./tests/files_for_testing/mapping.json', 'r'))

total_items = 0
for item in mapping_data:
	total_items = total_items + 1

lookup_all_data = json.load(open('./tests/files_for_testing/latest_all.json', 'r'))
abyssal_whip_lookup = json.load(open('./tests/files_for_testing/latest_aby_whip.json', 'r'))
timestamp_item = json.load(open('./tests/files_for_testing/timeseries.json', 'r'))

def test_build_item_list():
	item_list = structs.ItemList(mapping_data)
	assert len(item_list.item_list) == total_items
def test_get_item_from_lookup_id():
	item_list = structs.ItemList(mapping_data)
	item = item_list.generate_single_item(abyssal_whip_lookup['data'])
	assert type(item) == list and len(item) == 1 and item.pop().id == 4151 
def test_generate_list():
	item_list = structs.ItemList(mapping_data)
	items = item_list.generate_list(lookup_all_data['data'])
	assert type(items) == list and len(items) == total_items
def test_generate_list_skip():
	item_list = structs.ItemList(mapping_data)
	items = item_list.generate_list(lookup_all_data['data'], skip=True)
	assert type(items) == list and len(items) < total_items
def test_item_not_reference():
	item_list = structs.ItemList(mapping_data)
	first_item = item_list.generate_single_item(abyssal_whip_lookup['data'])
	second_item = item_list.generate_single_item(abyssal_whip_lookup['data'])
	assert first_item.pop() != second_item.pop()
def test_generate_timestamp_list():
	item_list = structs.ItemList(mapping_data)
	item_timestepped = item_list.generate_timestamp_list(timestamp_item['data'], 4151)
	assert type(item_timestepped) == list
def test_list_sorted():
	item_list = structs.ItemList(mapping_data)
	assert sorted(item_list, key=lambda item: item.id)

MOCK_ITEM_INFORMATION = {
	"examine": "Pudding",
	"id": 4151,
	"name": "abyssal whip",
	"value": 51515,
	"limit": 8000,
	"members": False,
	"lowalch": 1,
	"highalch": 2,
}
def test_item():
	item = structs.Item(MOCK_ITEM_INFORMATION)
	assert item.id == MOCK_ITEM_INFORMATION["id"]




# def test_valid_id():
# 	item_list: object = structs.ItemList()
# 	item = item_list.find(4151)
# 	assert item.name.lower() == "abyssal whip"
# def test_valid_id_given_str_id():
# 	item_list: object = structs.ItemList()
# 	identifier = '4151'
# 	item = item_list.find(int(identifier))
# 	assert item.name.lower() == "abyssal whip"
# def test_valid_name():
# 	item_list: object = structs.ItemList()
# 	item = item_list.find("abyssal whip")
# 	assert item is not None

# def test_pricing():
# 	mock_data = {
# 		'high': {
# 			'price': 500,
# 			'time': 11111
# 		},
# 		'low': {
# 			'price': 400,
# 			'time': 1110
# 		}
# 	}
# 	price_obj = structs.Pricing(mock_data)
# 	assert price_obj.high_price == 500