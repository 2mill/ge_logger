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

def test_itemlist():
	item_list = structs.ItemList()
	# assert len(item_list.find(4151)) == 1
	assert item_list.find(4151).name == "Abyssal whip"

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