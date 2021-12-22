
import argparse, json, requests 
import wikige
from structs import Item
from os.path import exists
import tools, commands
# first we will just be taking an id argument, and outputting the id's information high and low prices for the day.

args = commands.get_args()


if not exists("./item_data.json") or args.update:
	with open('./item_data.json', 'w') as f:
		json.dump(requests.get(
			tools.mapping_link,
			headers=tools.json_load("config.json")
		).json(), f)
		f.close()
# wiki_ge = WikiGe("config.json")


file_data = None
if args.update is not None:
	print(tools.download_items())
#If args.lookup is set, then lookup price information for the item.

if args.lookup is not None:
	# print(Item(wiki_ge.get_id(args.lookup, None)))
	item_data = wikige.get(args.lookup, None, './config.json')
	if item_data == {}:
		print("Item is non tradable, or not found")
	else:
		item = Item(item_data)
		print(item)
