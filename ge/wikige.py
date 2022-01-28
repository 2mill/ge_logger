import requests
from ge.structs import ItemList, PricedItem
from ge import utils
from ge import endpoints


class WikiGe():
	def __init__(self):
		self.item_list = ItemList()
	def lookup(self, identifier) -> PricedItem:
		# return utils.lookup(identifier)
		if type(identifier) is not int and type(identifier) is not str:
			raise ValueError("Lookup only accepts ints or strings")
		return utils.lookup(identifier, self.item_list)
	def lookup_all(self) -> PricedItem:
		utils.lookup_all(self.item_list)
		pass;


def get(key: str, timeseries: str, config_filepath) -> dict:
	items = tools.item_list("./item_data.json")
	item = tools.find_item(items, key)
	if item == []: return {}
	return tools.reformat(
		requests.get(
			tools.id_link(item[0]), 
			headers=tools.header(config_filepath)
		).json()['data'],
		item
	)