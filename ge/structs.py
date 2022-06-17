from typing import Iterable
from ge import endpoints
import json

# Remove this function. Not readable, bland, stupid.
give_it_back: str = lambda output, addition: f"{output}{addition}\n"
# TODO: Pricing data needs to be broken into two objects.
# The first object is just the pricing information.
# The second object should be able to handle avg pricing data from timesteps and timestamps
class Pricing:
	def __init__(self, pricing_data):
		self.high_price = pricing_data['high']['price']
		self.high_time = pricing_data['high']['time']
		self.low_price = pricing_data['low']['price']
		self.low_time = pricing_data['low']['time']

class ItemPricingInformation:
	id: int
	high:int
	highTime: int
	low: int
	lowTime: int
	def __init__(self, pricing_information):
		if  pricing_information != "{}":
			self.high = pricing_information['high']
			self.highTime = pricing_information['highTime']
			self.low = pricing_information['low']
			self.lowTime = pricing_information['lowTime']
class Item:
	name: str
	id: int
	examine: str
	members: bool
	low_alch: int
	high_alch: int
	limit: int
	value: int #Still not sure what this is
	pricing: ItemPricingInformation
	def __init__(self, item_information: json.JSONDecoder, item_pricing=None):
		self.examine = item_information['examine']
		self.id = item_information['id']
		self.name= item_information['name']
		self.members = item_information['members']
		self.value = item_information['value']
		# Some items do not have an alch information
		if 'lowalch' in item_information.keys():
			self.low_alch = item_information['lowalch']
			self.high_alch = item_information['highalch']
		else:
			self.low_alch, self.high_alch = None
		# Some items don't have limit information
		if 'limit' in item_information.keys():
			self.limit = item_information['limit']
		else: self.limit = None
		self.id = item_information['id']
		self.pricing = ItemPricingInformation(item_pricing[str(self.id)])

class ItemList(Iterable):
	def  __init__(self):
		self.item_list: list = []
		self.exchange_map = endpoints.mapping().json()
	def find(self, identifier:int) -> Item:
		"""Finds the item in the list, or returns None if it does not exist"""
		if type(identifier) != int: return ValueError
		item_information = list(
			filter(
				lambda data: data['id'] == identifier,
				self.exchange_map
		))
		if len(item_information) == 0:
			return None
		item_pricing = endpoints.latest(identifier).json()['data']
		return Item(item_information.pop(), item_pricing)
	def find_everything(self) -> list:
		item_pricing_information = endpoints.latest()['data']
		return [Item(item_information, item_pricing_information[item_information['id']]) for item_information in self.exchange_map]
	def __iter__(self) -> Iterable:
		self.everything().__iter__()