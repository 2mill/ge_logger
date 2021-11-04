import json, requests
from structs import Item





json_load: str = lambda location: json.load(open(f"./{location}", 'r'))
api_link = r"https://prices.runescape.wiki/api/v1/osrs/"
mapping_link = f"{api_link}mapping"
id_link = lambda id: f"{api_link}latest?id={id}"



def id_dict(filename: str) -> dict:
	item_data: json = json_load(f"./{filename}")
	item_dictionary: dict = {}
	for item in item_data:
		item_dictionary[item['id']] = item['name']
	return item_dictionary
class WikiGe:
	def __init__(self, config_filepath) -> None:
		header_config = json_load(config_filepath)
		self.header = {
			'User-agent': header_config['user-agent'],
			'From': header_config['email']
		}
		self.id_dict = id_dict("item_data.json")
	def get_id(self, id: int, timeseries: str) -> object:
		link = id_link(id)
		info = requests.get(link, self.header).json()
	def get_mapping(self) -> object:
		request = requests.get(mapping_link, headers=self.header)
		if (request.status_code == 404): print("Got a 404")
		return request.json()

def wiki_ge(config_filepath: str) -> object: 
	header_config = config(config_filepath)
	header: object = lambda config: {
		'User-agent': header_config['user-agent'],
		'From': header_config['email']
	}
	# At this point I have misspelled it too much for me to fix it...
	return wikie_ge