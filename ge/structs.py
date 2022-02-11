from typing import Iterable
import requests as req
import json

# Remove this function. Not readable, bland, stupid.
give_it_back: str = lambda output, addition: f"{output}{addition}\n"
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
		if data != "{}":
			self.high = data['high']
			self.highTime = data['highTime']
			self.low = data['low']
			self.lowTime = data['lowTime']

class ItemPricingInformationList:
	def __init__(self, item_pricing_list):
		self.item_list = []
		for item in item_pricing_list:
			self.item_list.append(ItemPricingInformation(int(item),item_pricing_list[item]))
		self.item_list.sort(key=lambda item: item.id)
	def find_id(self, id:int):
		for item in self.item_list:
			if item.id == id: return item
		return None

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
	def __init__(self, item_information):
		self.examine = item_information['examine']
		self.name= item_information['name']
		self.id = item_information['id']
		self.members = item_information['members']
		self.value = item_information['value']
		self.raw_dict = item_information

		# Some items do not have an alch information
		if 'lowalch' in item_information.keys():
			self.low_alch = item_information['lowalch']
			self.high_alch = item_information['highalch']
		else:
			self.low_alch = None
			self.high_alch = None
		# Some items don't have limit information
		if 'limit' in item_information.keys():
			self.limit = item_information['limit']
		else: self.limit = None
		self.pricing = None
	def set_pricing(self, itempricinginformation:ItemPricingInformation):
		self.pricing = itempricinginformation
	def __copy__(self) -> object:
		## Write tests for this copy function.
		return Item(self.raw_dict)

class ItemList(Iterable):
	def  __init__(self,exchange_map):
		self.item_list: list = []
		# exchange_map = req.get(endpoint, headers=header).json()
		for item_info in exchange_map:
			temp_item = Item(item_info)
			self.item_list.append(temp_item)
		self.item_list.sort(key=lambda item: item.id)
	def generate_list(self, item_pricing) -> list:
		new_list: list = []
		for item in self.item_list:
			item_id_str: str = str(item.id)
			pricing_information = item_pricing[item_id_str]
			new_item: Item = item.__copy__()
			new_item.set_pricing(pricing_information)
			new_list.append(new_item)
		return new_list
	def generate_single_item(self, item_pricing) -> list:
		for item_id_str in item_pricing:
			item_id_int: int = int(item_id_str)
			item = self.find(item_id_int)
			if item is None: return []
			item: Item = item.__copy__()
			item.set_pricing(item_pricing)	
			return [item]
	def generate_timestamp_list(self, item_pricing, item_id: int):
		item: Item = self.item_list.find(item_id)
		new_list:list = []
		for pricing in item_pricing:
			temp_item = item.__copy__()
			temp_item.set_pricing(pricing)
			new_list.append(temp_item)
		return new_list

		

	def _timestep_list_generation(self, item_pricing, timeste_id) -> list:
		"""timsteps are different, because they do not pass the id."""
		raise NotImplementedError
	def find_id(self, identifier: int):
		for item in self.item_list: 
			if item.id == identifier: return item
		return None
	def find_name(self, name:str):
		for item in self.item_list:
			if item.name == name: return item
		return None
	def __iter__(self):
		return ItemListIterator(self)


	def find(self, identifier) -> Item:
		if type(identifier) == str: return self.find_name(identifier)
		if type(identifier) == int: return self.find_id(identifier)
class ItemListIterator:
	def __init__(self, item_list:ItemList):
		self.item_list = item_list.item_list
		self.index = -1
	def __next__(self):
		self.index = self.index + 1
		actual_index = self.index + 1
		if actual_index == len(self.item_list):
			raise StopIteration
		else:
			return self.item_list[self.index]