from typing import Iterable
<<<<<<< HEAD:ge/structs.py
from ge import endpoints
import json

# Remove this function. Not readable, bland, stupid.
give_it_back: str = lambda output, addition: f"{output}{addition}\n"
class Pricing:
	def __init__(self, pricing_data):
		self.high_price = pricing_data['high']['price']
		self.high_time = pricing_data['high']['time']
		self.low_price = pricing_data['low']['price']
		self.low_time = pricing_data['low']['time']

=======
>>>>>>> main:wikige/structs.py
class ItemPricingInformation:
	id: int
	high:int
	high_time: int
	low: int
<<<<<<< HEAD:ge/structs.py
	lowTime: int
	def __init__(self, identifier:int, pricing_information: json.JSONDecodeError):
		self.id = identifier
=======
	low_time: int
	def __init__(self, pricing_information):
>>>>>>> main:wikige/structs.py
		if  pricing_information != "{}":
			self.high = pricing_information['high']
			self.high_time = pricing_information['highTime']
			self.low = pricing_information['low']
<<<<<<< HEAD:ge/structs.py
			self.lowTime = pricing_information['lowTime']

class TimedItemPricingInformation:
	avg_high_price: int
	avg_low_price: int
	high_volume:int
	low_volume: int
	id: int
	timestamp: int
	def __init__(self, identity, pricing_information, timestamp: int):
		self.id = identity
		self.avg_high_price = pricing_information['avgHighPrice']	
		self.avg_low_price = pricing_information['avgLowPrice']	

		self.high_volume= pricing_information['highPriceVolume']	
		self.low_volume= pricing_information['lowPriceVolume']	

		self.timestamp = timestamp

=======
			self.low_time = pricing_information['lowTime']
>>>>>>> main:wikige/structs.py
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
	def __init__(self, item_information: json.JSONDecoder):
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
			self.low_alch, self.high_alch = [None, None]
		# Some items don't have limit information
		if 'limit' in item_information.keys():
			self.limit = item_information['limit']
		else: self.limit = None
<<<<<<< HEAD:ge/structs.py
=======
		self.pricing = None
	def set_pricing(self, itempricinginformation:ItemPricingInformation):
		self.pricing = ItemPricingInformation(itempricinginformation)
	def __copy__(self) -> object:
		## Write tests for this copy function.
		return Item(self.raw_dict)
>>>>>>> main:wikige/structs.py

class ItemList(Iterable):
	def  __init__(self, exchange_map:list):
		self.item_list: list[Item]= [Item(item_information) for item_information in exchange_map]
	def find(self, identifier:int) -> Item:
		"""Finds the item in the list, or returns None if it does not exist"""
		if type(identifier) != int: return ValueError
		for item in self.item_list:
<<<<<<< HEAD:ge/structs.py
=======
			item_id_str: str = str(item.id)
			pricing_information = None
			try:
				pricing_information = item_pricing[item_id_str]
			except KeyError:
				if skip:
					continue
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
		item: Item = self.find(item_id)
		new_list:list = []
		for pricing in item_pricing:
			temp_item = item.__copy__()
			temp_item.set_pricing(pricing)
			new_list.append(temp_item)
		return new_list
	def find_id(self, identifier: int):
		for item in self.item_list: 
>>>>>>> main:wikige/structs.py
			if item.id == identifier: return item
		return None
	def __iter__(self) -> Iterable:
		return self.item_list.__iter__()