import json 





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

def wiki_ge(config_filepath: str) -> object: 
	header_config = config(config_filepath)
	header: object = lambda config: {
		'User-agent': header_config['user-agent'],
		'From': header_config['email']
	}
	# At this point I have misspelled it too much for me to fix it...
	return wikie_ge