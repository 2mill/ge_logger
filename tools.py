import json, requests







json_load: str = lambda location: json.load(open(f"./{location}"))
# json_request: json = lambda url, header: json.load(requests.get(location, headers=header))
api_link:str = r"https://prices.runescape.wiki/api/v1/osrs/"
mapping_link:str = f"{api_link}mapping"
id_link = lambda id: f"{api_link}latest?id={id}"
format_commas_gp: str = lambda price: "{:,}gp".format(price)
def id_dict(filename: str) -> dict:
	item_data: json = json_load(f"./{filename}")
	item_dictionary: dict = {}
	for item in item_data:
		item_dictionary[item['id']] = item['name']
	return item_dictionary
