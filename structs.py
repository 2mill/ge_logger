from tools import json_load, id_dict
import tools
import requests
from datetime import date
import datetime

# Remove this function. Not readable, bland, stupid.
give_it_back: str = lambda output, addition: f"{output}{addition}\n"
date.fromtimestamp(555)



class Item:
	def __init__(self, item_data):
		self.item_data = item_data
		self.name = item_data['name']
		self.id = item_data['id']
		self.high_price = {
			'price': item_data['pricing']['high'],
			'time': item_data['pricing']['highTime']
		}
		self.low_price = {
			'price': item_data['pricing']['low'],
			'time': item_data['pricing']['lowTime']
		}

	def __str__(self) -> str:
		return "{}:{}".format(self.name, self.id)
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
		return reformat(item_data)

	def _reformat(item_data: dict) -> dict:
		"""
			Not the biggest fan of how OSRS Wiki formats their json.
			Therefore, I reformat it to make it more human readable.
		"""
		# Extracts the id from the dictionary as a string
		id = list(item_data.keys())[0]
		# TODO: Add a time delta
		return {
			'id' : str(id),
			'name' : item_data[id],
			'pricing': {
				'high': {
					'price': item_data[id]['high'],
					'time': item_data[id]['highTime']
				},
				'low': {
					'price': item_data[id]['low'],
					'time': item_data[id]['lowTime']
				}
			}
		}
	def get_name(self, name:str, timeseries: str) -> dict:
		for id in list(self.id_dict.keys):
			# If the dictionary item matches the name, then plug it into get_id
			if self.id_dict[id] == name: return self.get_id(id, timeseries)

	def get_mapping(self) -> object:
		request = requests.get(mapping_link, headers=self.header)
		if (request.status_code == 404): print("Got a 404")
		return request.json()