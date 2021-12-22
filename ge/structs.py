import tools
import math
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
			'time': item_data['pricing']['high']['time']
		}
		self.low_price = {
			'price': item_data['pricing']['low']['price'],
			'time': item_data['pricing']['low']['time']
		}

	def __str__(self) -> str:
		return "{}:{}".format(self.name, self.id)


class PriceData:
	def __init__(self, pricing_data: list):
		self.high_price = pricing_data[0]
		self.high_time = pricing_data[1]
		self.low_price = pricing_data[2]
		self.low_time = pricing_data[3]
		#TODO: FIgure calculate change in price.
