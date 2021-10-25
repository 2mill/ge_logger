import requests
class Item:
	def __init__(self, name, id):
		self.name = name
		self.id = id
		item_data = requests.get(id_url(id), headers=header).json()
		self.high = item_data['data'][f'{id}']['high']
		self.low = item_data['data'][f'{id}']['low']

	def __str__(self) -> str:
		pass