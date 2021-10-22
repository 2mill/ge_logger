
import argparse, requests, json
# first we will just be taking an id argument, and outputting the id's information high and low prices for the day.

parser = argparse.ArgumentParser(prog="ge_track", description="Used for checking the item low and high price for a certain ID")
parser.add_argument("--id", type=int, required=True, help="Item ID. Returns an error if the item was not found");

args = parser.parse_args();

print(args.id)


id_url = f"https://prices.runescape.wiki/api/v1/osrs/latest?id={args.id}"
header = {
	'User-Agent': 'My personal ge price tracker',
	'From': 'yannick.dorn@gmail.com'
}
item_map = requests.get(f"https://prices.runescape.wiki/api/v1/osrs/mapping", headers=header)
item_map = item_map.json()
with open('item_data.json', 'w') as outfile:
	json.dump(item_map, outfile)