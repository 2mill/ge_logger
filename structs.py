from tools import json_load, id_dict
import tools
import requests
from datetime import date

class Item:
	def __init__(self, item_data):
		self.item_data = item_data
		self.item_data['timestamp'] = date.today()
	def __str__(self) -> str:
		output = f"{self.item_data['id']}\pricing: {self.item_data['pricing']}\n"
		return output
class WikiGe:
	def __init__(self, config_filepath:str) -> None:
		header_config = json_load(config_filepath)
		self.header = {
			'User-agent': header_config['user-agent'],
			'From': header_config['email']
		}
		self.id_dict: dict = id_dict("item_data.json")
	def get_id(self, id: int, timeseries: str) -> dict:
		link:str = tools.id_link(id)
		info = requests.get(link, headers=self.header).json()
		item_data: dict = {
			'id': str(id),
			'pricing': info['data'][str(id)]
		}
		# item_data: dict = info['data']
		return item_data
	def get_name(self, name:str, timeseries: str) -> dict:
		for id in list(self.id_dict.keys):
			# If the dictionary item matches the name, then plug it into get_id
			if self.id_dict[id] == name: return self.get_id(id, timeseries)

	def get_mapping(self) -> object:
		request = requests.get(mapping_link, headers=self.header)
		if (request.status_code == 404): print("Got a 404")
		return request.json()