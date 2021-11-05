
import argparse, json 
import requests
import tools
from structs import Item, WikiGe
from os.path import exists
# first we will just be taking an id argument, and outputting the id's information high and low prices for the day.

parser = argparse.ArgumentParser(prog="ge_track", description="Used for checking the item low and high price for a certain ID")
parser.add_argument('--update', action="store_true", required=False, help="Updates the list for new item information")
parser.add_argument('--lookup', type=str, required=False, help="Looks up an item given an ID number or item name")
parser.add_argument('--init', action="store_true", required=False, help="Initialize the configuration fil")
parser.add_argument('--track', type=str, required=False, help="Start tracking an item, latest price data if not given.")
parser.add_argument('--price', type=int, required=False, help="The price of the tracked item.")
args = parser.parse_args();


wiki_ge = WikiGe("./config.json")

if not exists("./ge_tracker.json"):
	with open('./ge_tracker.json', 'w') as f:
		f.close()


# If already exists, then don't download more data unless the argument has been made for more data.
if not exists("./item_data.json") or args.update:
	with open('item_data.json', 'w') as outfile:
		json.dump(wiki_ge.get_mapping(), outfile)
file_data = None
#If args.lookup is set, then lookup price information for the item.
if args.lookup is None:
	print(Item(wiki_ge.get_id(int(args.lookup))))
