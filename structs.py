class Item:
	def __init__(self, id:int, name:str, info:object):
		self.id = id
		self.info = info
		self.high = item_data['data'][f'{id}']['high']
		self.low = item_data['data'][f'{id}']['low']
	def __str__(self) -> str:
		pass
class Player:
	def __init__(self, name):
		self.name = name
		self.items = []

	def track_item(self, id: int, price) -> bool:
		item = {
			"item": Item(id),
			"purchase_price": price
		}
		self.items.append(item)