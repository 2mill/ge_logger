import requests
from ge.structs import Item


class WikiGe():
	def __init__():
		self.description = "WIKIGE"
		
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