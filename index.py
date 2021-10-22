
import argparse, requests, json 
from os.path import exists
# first we will just be taking an id argument, and outputting the id's information high and low prices for the day.

parser = argparse.ArgumentParser(prog="ge_track", description="Used for checking the item low and high price for a certain ID")
parser.add_argument("--id", type=int, required=True, help="Item ID. Returns an error if the item was not found");
parser.add_argument('--update', action="store_true", required=False, help="Updates the list for new item information")
args = parser.parse_args();

print(args.id)



id_url = f"https://prices.runescape.wiki/api/v1/osrs/latest?id={args.id}"
header = {
	'User-Agent': 'My personal ge price tracker',
	'From': 'yannick.dorn@gmail.com'
}
item_map = requests.get(f"https://prices.runescape.wiki/api/v1/osrs/mapping", headers=header)
item_map = item_map.json()
# If already exists, then don't download more data unless the argument has been made for more data.
if not exists("./item_data.json") or args.update:
	print('ran')
	with open('item_data.json', 'w') as outfile:
		json.dump(requests.get(f"https://prices.runescape.wiki/api/v1/osrs/mapping").json(), outfile)


file_data = None
with open('./item_data.json', 'r') as data:
	file_data = json.load(data)

for item in file_data:
	if item['id'] == args.id:
		item_information_get = requests.get(id_url, headers=header).json()
		print(item['name'])
		print(item_information_get['data'][f'{args.id}']['high'])
		print(item_information_get['data'][f'{args.id}']['low'])



