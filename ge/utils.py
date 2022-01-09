import json
import re
from endpoints import get_latest, get_mapping, get_timestep
from osrsbox import items_api

from ge.structs import Item


class ItemList:
	def __init__(self):
		self.item_list = items_api.load()
	def find_id(id: int) -> object: 
		for item in self.item_list:
			if item.id == id: return item
		return None
	def find_name(name: str) -> object:
		for item in self.item_list:
			if item.name.lower() == name.lower(): return item
		return None
	

class ItemInfo:
	def __init__(self):




is_id: bool = lambda input: re.match(r"^\d+$", input) is not None
json_load: str = lambda location: json.load(open(f"./{location}"))

api_link:str = r"https://prices.runescape.wiki/api/v1/osrs/"

# json_request: json = lambda url, header: json.load(requests.get(location, headers=header))
format_commas_gp: str = lambda price: "{:,}gp".format(price)

# Simple function where the item data is pulled down.

def valid_item(id: int) -> bool:
	osrs
def download_items() -> bool:
	osrsbox_endpoint: str = r"https://www.osrsbox.com/osrsbox-db/items-search.json"
	item_data = requests.get(osrsbox_endpoint)
	if item_data.status_code >= 400:
		return False
	with open("./data/item_data.json", 'w') as f:
		json.dump(item_data.json(), f)
	return True

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



# def get_name(item_list:list, name:str) -> tuple(Item, None):
# 	for item in item_list:
# 		if item.name == name:
# 			return get_id(item)
# 	return None
def get_id(item_list: list, identifier):
	#idenftifier can either be the name or id of the item.
	if isinstance(identifier, str): identifier = identifier.lower()
	for item in item_list:
		if item.name.lower() == identifier or item.id == identifier:
			item_data = requests.get(
				id_link(item.id),
				headers=header
			).json()
			formatted = reformat(
				item_data['data'],
				[item.id, item.name]
			)
			return Item(formatted)
	return None
def reformat(item_data: dict, item:list) -> dict:
	"""
		Not the biggest fan of how OSRS Wiki formats their json.
		Therefore, I reformat it to make it more human readable.
	"""
	id_num, name = item
	id_num = str(id_num)
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
