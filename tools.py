import json, requests
from structs import Item





config: str = lambda location: json.load(open(f"./{location}", 'r'))
id_link = lambda id: f"https://prices.runescape.wiki/api/osrs/latest?id={id}"
mapping_link = r"https://prices.runescape.wiki/api/v1/osrs/mapping"
def id_map() -> map:
	file_data = None
	with open("./item_data.json", 'r') as data:
		file_data = json.load(data)
	ids = []
	names = []
	for item in file_data:
		ids.append(item['id'])
		names.append(item['name'])
	id_map = map(lambda id, name: name, ids, names)
	return id_map
class WikiGe:
	def __init__(self, config_filepath) -> None:
		header_config = config(config_filepath)
		self.header = {
			'User-agent': header_config['user-agent'],
			'From': header_config['email']
		}
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