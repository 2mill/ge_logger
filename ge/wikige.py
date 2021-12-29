import tools
import requests
from structs import Item


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
def get_mapping(self) -> object:
	request = requests.get(tools.mapping_link, headers=self.header)
	if (request.status_code == 404): print("Got a 404")
	return request.json()