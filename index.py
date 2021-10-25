
import argparse, requests, json 
from tools import wiki_ge
from structs import Item
from os.path import exists
MAPPING_URL = "https://prices.runescape.wiki/api/v1/osrs/mapping"
# first we will just be taking an id argument, and outputting the id's information high and low prices for the day.

parser = argparse.ArgumentParser(prog="ge_track", description="Used for checking the item low and high price for a certain ID")
parser.add_argument('--update', action="store_true", required=False, help="Updates the list for new item information")
parser.add_argument('--lookup', type=str, required=False, help="Looks up an item given an ID number or item name")
args = parser.parse_args();


wiki_ge = wiki_ge("./config.json")
# If already exists, then don't download more data unless the argument has been made for more data.
if not exists("./item_data.json") or args.update:
	with open('item_data.json', 'w') as outfile:
		json.dump(requests.get(wiki_ge.mapping_link).json(), outfile)


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