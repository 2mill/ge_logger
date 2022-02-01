from osrsbox import items_api
import osrsbox

# Remove this function. Not readable, bland, stupid.
give_it_back: str = lambda output, addition: f"{output}{addition}\n"
class Pricing:
	def __init__(self, pricing_data):
		self.high_price = pricing_data['high']['price']
		self.high_time = pricing_data['high']['time']
		self.low_price = pricing_data['low']['price']
		self.low_time = pricing_data['low']['time']


class ItemList:
	def __init__(self):
		self.item_list: list = items_api.load()

	def find_id(self, id: int) -> object: 
		for item in self.item_list:
			if item.id == id: return item
		return None
		# Still wondering if I should return or raise here.
	def find_name(self, name: str) -> object:
		for item in self.item_list:
			if item.name.lower() == name.lower(): return item
		return None
	def find(self, identifier) -> object:
		if type(identifier) is int: return self.find_id(identifier)
		elif type(identifier) is str: return self.find_name(identifier)
class Item:
	identifier: int
	name: str
	pricing: Pricing
	def __init__(self, identifier=None, name=None, pricing=None):
		self.id = identifier
		self.name = name
		self.pricing = None
	def set_pricing(self,pricing: Pricing):
		self.pricing = pricing
