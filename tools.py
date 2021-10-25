import json, requests





config: str = lambda location: json.load(open(f"./{location}", 'r'))

def wiki_ge(config_filepath: str) -> object: 
	header_config = config(config_filepath)
	header: object = lambda config: {
		'User-agent': header_config['user-agent'],
		'From': header_config['email']
	}
	wikie_ge: object = {}
	wikie_ge.id_link = lambda id: f"https://prices.runescape.wiki/api/osrs/latest?id={id}"
	wikie_ge.mapping_link = f"https://prices.runescape.wiki/api/osrs/mapping"
	wikie_ge.id_latest = lambda id: requests.get(wikie_ge.id_link(id), headers=header)
	# At this point I have misspelled it too much for me to fix it...
	return wikie_ge