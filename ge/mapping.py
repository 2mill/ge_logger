from xml.dom.minidom import Identified
import requests as req
endpoint = "https://prices.runescape.wiki/api/v1/osrs/mapping"





class Item:
	name: str
	id: int
	examine: str
	members: bool
	low_alch: int
	high_alch: int
	limit: int
	value: int #Still not sure what this is
	high_price: int
	high_time: int
	low_price: int
	low_time:int
	def __init__(self, item_information, pricing=None):
		self.examine = item_information['examine']
		self.name= item_information['name']
		self.id = item_information['id']
		self.members = item_information['members']
		self.value = item_information['value']

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


		if pricing is not None:
			pass


class ItemList:
	def  __init__(self, add_pricing=False):
		self.item_list = []
		header = {
			'User-agent': '2mill/osrs_exchange'
		}
		exchange_map = req.get(endpoint, headers=header).json()
		for item_info in exchange_map:
			self.item_list.append(Item(item_info))
	def _find_id(self, identifier: int):
		for item in self.item_list: 
			if item.id == identifer: return item
		return None
	def _find_name(self, name:str):
		for item in self.item_list:
			if item.name == identifier: return item
		return None

	def find(self, identifier) -> Item:
		if type(identifier) == str: return self._find_name(identifier)
		if type(identifier) == int: return self._find_id(identifier)