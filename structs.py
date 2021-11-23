from tools import json_load, id_dict
import tools
import requests
from datetime import date
import datetime
give_it_back: str = lambda output, addition: f"{output}{addition}\n"
date.fromtimestamp(555)


def set_dates(pricing: dict) -> dict:
	"""
	Take item data information and assign date objects to the highTime and lowTIme dict
	Returns a new dict object
	"""

	# TODO:Proper error handling for invalid input
	pricing_types = [
		'high',
		'low'
	]
	for type in pricing_types:
		print(pricing[f'{type}Time'])
		
		pricing[f'{type}Time'] = date.fromtimestamp(pricing[f'{type}Time'])
	return pricing
class Item:
	def __init__(self, item_data):
		self.item_data = item_data
		print(self.item_data['pricing']['highTime'])
		if self.item_data is not None:
			self.item_data['int_timestamp'] = date.today()
	def __str__(self) -> str:
		if self.item_data is None:
			return "DNE"
		output = give_it_back("", self.item_data['name'])
		output = give_it_back(
			"",
			f"{self.item_data['name']}:{self.item_data['id']}"
		)
		output = give_it_back(output, "PRICING DATA:")

		# TODO: Figure out why strftime is not working properly.
		format: str = r"%d/%m/%Y %X"
		high_low: list = ['high', 'low']
		template: str = "{}: {} at {}"
		# Fucked shit up here and now I am tired.
		# Responsiblities for tomorrw's me.
		for version in high_low:
			template.format(
				version.upper(),
				tools.format_commas_gp(self.item_data['pricing'][version]),
				self.item_data['pricing'][f'{version}Time'].strftime(format)
			)
			output = give_it_back(output, template)


		output = give_it_back(
			output,
			f"HIGH: {tools.format_commas_gp(self.item_data['pricing']['high'])} at {self.item_data['pricing']['highTime'].strftime(format)}"
		)
		output = give_it_back(
			output,
			f"LOW: {tools.format_commas_gp(self.item_data['pricing']['low'])} at {self.item_data['pricing']['lowTime'].strftime(format)}"
		)
		# This still needs to be figured out.
		# ouput = give_it_back(
		# 	output,
		# 	f"TIME SPAN:{date.now()}"
		# )
		# output = f"{self.item_data['id']}pricing: {self.item_data['pricing']}\n"
		# output = f"{output}high:{tools.format_commas_gp(self.item_data['pricing']['high'])}"
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
		try:
			item_data: dict = {
				'id': id,
				'name': self.id_dict[int(id)],
				'pricing': set_dates(info['data'][id])
			}
		except KeyError:
			return None
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