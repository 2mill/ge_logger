from argparse import ArgumentParser
def get_args() -> ArgumentParser:
	parser = ArgumentParser(prog="ge_track", description="Used for checking the item low and high price for a certain ID")
	parser.add_argument('--update', action="store_true", required=False, help="Updates the list for new item information")
	parser.add_argument('--lookup', type=str, required=False, help="Looks up an item given an ID number or item name")
	parser.add_argument('--init', action="store_true", required=False, help="Initialize the configuration fil")
	parser.add_argument('--track', type=str, required=False, help="Start tracking an item, latest price data if not given.")
	parser.add_argument('--price', type=int, required=False, help="The price of the tracked item.")

	return parser.parse_args()



