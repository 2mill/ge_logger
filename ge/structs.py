import math
from datetime import date
from osrsbox import items_api

# Remove this function. Not readable, bland, stupid.
give_it_back: str = lambda output, addition: f"{output}{addition}\n"
class Item:
	def __init__(self, item_data):
		self.name = item_data['name']
		self.id = item_data['id']
		self.buy_price = {
			'price': item_data['pricing']['high']['price'],
			'time': item_data['pricing']['high']['time']
		}
		self.sell_price = {
			'price': item_data['pricing']['low']['price'],
			'time': item_data['pricing']['low']['time']
		}

		# History behaves as a cache.
		# If the user wants to update the item,
		# The item will remember its previous entries.
		self.history = []
		# self.high_price = {
		# 	'price': item_data['pricing']['high']['price'],
		# 	'time': item_data['pricing']['high']['time']
		# }
		# self.low_price = {
		# 	'price': item_data['pricing']['low']['price'],
		# 	'time': item_data['pricing']['low']['time']
		# }

	def __str__(self) -> str:
		return "{}:{}".format(self.name, self.id)


class PriceData:
	def __init__(self, pricing_data: list):
		self.high_price = pricing_data[0]
		self.high_time = pricing_data[1]
		self.low_price = pricing_data[2]
		self.low_time = pricing_data[3]
		#TODO: FIgure calculate change in price.
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
