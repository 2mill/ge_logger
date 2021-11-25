import tools
import requests
from structs import Item

def _get_header(config_filepath: str) -> dict:
	config = tools.json_load(config_filepath)
	return {
		'User-agent': config['user-agent'],
		'From': header_config['email']
	}

def get(key: str, timeseries: str, config_filepath) -> dict:
	items = tools.item_list("./item_data.json")
	item = tools.find_item(items, key)
	if item == []: return {}
	return tools.reformat(
		requests.get(
			tools.id_link(item[0]), 
			headers=tools.header(config_filepath)
		).json()['data']
	)
def get_mapping(self) -> object:
	request = requests.get(tools.mapping_link, headers=self.header)
	if (request.status_code == 404): print("Got a 404")
	return request.json()