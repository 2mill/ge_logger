import json, requests
import re

is_id: bool = lambda input: re.match(r"^\d+$", input) is not None
json_load: str = lambda location: json.load(open(f"./{location}"))
def header(config_filepath: str) -> dict:
	file = json_load(config_filepath)
	return {
		'User-agent': file['user-agent'],
		'email': file['email']
	}

# json_request: json = lambda url, header: json.load(requests.get(location, headers=header))
api_link:str = r"https://prices.runescape.wiki/api/v1/osrs/"
mapping_link:str = f"{api_link}mapping"
id_link = lambda id: f"{api_link}latest?id={id}"
format_commas_gp: str = lambda price: "{:,}gp".format(price)

def item_list(filename: str) -> list:
	items = []
	# TODO: Datacashing, use timedeltas to update cache as needed.
	item_data: json = json_load(f"./{filename}")
	for item in item_data:
		items.append(
			[
				str(item['id']),
				item['name'],
			]
		)
	# sorted(items, key=lambda item: item[0])
	return items
# TODO: Proper config file saving into the correct path.


def find_item(items: list, identifier: str) -> list:
	for i in range(len(items)):
		item = items[i]
		if item[0] == identifier or item[1].lower() == identifier:
			return item
	return []

	# TODO: IMPLEMENT BINARY SEARCH FROM HERE:
	# http://www.rosettacode.org/wiki/Binary_search#Python:_Recursive
	"""
		Due to the nature of my list structure,
		and me not wanting to figure out sort properly.
		I need to implement my own split search.
	"""

def reformat(item_data: dict, item:list) -> dict:
	"""
		Not the biggest fan of how OSRS Wiki formats their json.
		Therefore, I reformat it to make it more human readable.
	"""
	id_num, name = item
	# TODO: Add a time delta
	return {
		'id' : id_num,
		'name' : name,
		'pricing': {
			'high': {
				'price': item_data[id_num]['high'],
				'time': item_data[id_num]['highTime']
			},
			'low': {
				'price': item_data[id_num]['low'],
				'time': item_data[id_num]['lowTime']
			}
		}
	}
