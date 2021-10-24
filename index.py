
import argparse, requests, json 
from os.path import exists
MAPPING_URL = "https://prices.runescape.wiki/api/v1/osrs/mapping"
# first we will just be taking an id argument, and outputting the id's information high and low prices for the day.

parser = argparse.ArgumentParser(prog="ge_track", description="Used for checking the item low and high price for a certain ID")
parser.add_argument('--update', action="store_true", required=False, help="Updates the list for new item information")
parser.add_argument('--lookup', type=str, required=False, help="Looks up an item given an ID number or item name")
args = parser.parse_args();





if args.lookup is not None and args.lookup.isnumeric():
	args.lookup = int(args.lookup)
# id_url = f"https://prices.runescape.wiki/api/v1/osrs/latest?id={args.id}"
id_url = lambda id: f"https://prices.runescape.wiki/api/v1/osrs/latest?id={id}"
header = {
	'User-Agent': 'My personal ge price tracker',
	'From': 'yannick.dorn@gmail.com'
}
class Item:
	def __init__(self, name, id):
		self.name = name
		self.id = id
		item_data = requests.get(id_url(id), headers=header).json()
		self.high = item_data['data'][f'{id}']['high']
		self.low = item_data['data'][f'{id}']['low']

	def __str__(self) -> str:

item_map = requests.get(f"https://prices.runescape.wiki/api/v1/osrs/mapping", headers=header)
item_map = item_map.json()
# If already exists, then don't download more data unless the argument has been made for more data.
if not exists("./item_data.json") or args.update:
	with open('item_data.json', 'w') as outfile:
		json.dump(requests.get(f"https://prices.runescape.wiki/api/v1/osrs/mapping").json(), outfile)


file_data = None


#If args.lookup is set, then lookup price information for the item.
if args.lookup is not None:
	with open('./item_data.json', 'r') as data:
		file_data = json.load(data)
	for item in file_data:
		if item['id'] == args.lookup or item['name'].lower() == args.lookup.lower():
			item_information_get = requests.get(id_url(item['id']), headers=header).json()
			item = Item(item['name'], item['id'])
			print(item.high)
			print(item.low)