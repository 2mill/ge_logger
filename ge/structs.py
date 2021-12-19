import tools
import requests
import datetime
from datetime import date

# Remove this function. Not readable, bland, stupid.
give_it_back: str = lambda output, addition: f"{output}{addition}\n"
class Item:
	def __init__(self, item_data):
		self.item_data = item_data
		self.name = item_data['name']
		self.id = item_data['id']
		self.high_price = {
			'price': item_data['pricing']['high']['price'],
			'time': item_data['pricing']['high']['price']
		}
		self.low_price = {
			'price': item_data['pricing']['low']['price'],
			'time': item_data['pricing']['low']['time']
		}

	def __str__(self) -> str:
		return "{}:{}".format(self.name, self.id)