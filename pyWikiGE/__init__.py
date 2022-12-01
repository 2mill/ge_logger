import requests
from enum import Enum
from pyWikiGE.structs import LatestItem, MappedItem, TimedItem
from pyWikiGE.structs import ItemPriceInterval
from pyWikiGE.utils import EndpointBuilder
HEADER = {"User-agent": "github.com/2mill/osrs_exchange"}

class Game(Enum):
	OSRS='osrs'
	DeadManMode='dmm'
	FreshStart='fsw'

class Client:
	item_map: dict

	def __init__(self) -> None:
		res = EndpointBuilder(
			'mapping',
		).fetch()

		data: dict = None
		if res.ok:
			data: dict = res.json()

		self.item_map = {}

		for item in data:

			item: dict = item
			item_id = str(item.get('id'))
			self.item_map[item_id] = item

	def latest(self, id=None) -> list[LatestItem]:
		endpoint = "/latest"
		if id:
			endpoint += "?id={}".format(id)

		params = {
			'id': id
		}


		res = EndpointBuilder(endpoint, params).fetch()
		data = None
		if not res.ok:
			return None


		data: dict = res.json()
		data = data.get('data')
		packaged_items: list[LatestItem] = []
		for item in data:
			item_data = data.get(item)
			packaged_item = LatestItem(
				id = int(item),
				high = item_data.get('high'),
				low = item_data.get('low'),
				high_time = item_data.get('highTime'),
				low_time = item_data.get('low_time')
			)
			packaged_items.append(packaged_item)
		return packaged_items


	def mapping(self) -> list[MappedItem]:
		res = EndpointBuilder('mapping').fetch()
		if not res.ok:
			return None

		data = res.json()

		packaged_items: list[MappedItem] = []

		for item in data:
			packaged_item = MappedItem(
				id = item.get('id'),
				name = item.get('name'),
				value = item.get('value'),
				members = item.get('members'),
				low_alch = item.get('lowalch'),
				high_alch = item.get('highalch'),
				limit = item.get('limit'),
				examine = item.get('examine'),
				icon = item.get('icon')
			)
			packaged_items.append(
				packaged_item
			)

		return packaged_items
	def timeseries(self, id:int, timestep:str) -> TimedItem:

		params = {
			'id': id,
			'timestep': timestep
		}
		res = EndpointBuilder(
			'timeseries',
			params
		).fetch()

		if not res.ok: return None

		data: dict = res.json()



		listed_price_points: list[ItemPriceInterval] = []

		for price_point in data.get('data'):
			price_point: dict = price_point
			interval = ItemPriceInterval(
				price_point.get('timestamp'),
				price_point.get('avgHighPrice'),
				price_point.get('avgLowPrice'),
				price_point.get('highPriceVolume'),
				price_point.get('lowPriceVolume')
				
			)

		return TimedItem(
			id,
			listed_price_points
		)
	def timestamp(self, timestep: str) -> list[TimedItem]:
		res = EndpointBuilder(
			timestep
		).fetch()

		if not res.ok:
			return None

		data: dict = res.json()

		timestamp: int = data.get('timestamp')
		items: dict = data.get('data')
		packaged_items: list[TimedItem]= []

		for item in items:
			item_id = item
			item = items.get(item)
			price_point: list[ItemPriceInterval]= [
				ItemPriceInterval(
					timestamp,
					item.get('avgHighPrice'),
					item.get('avgLowPrice'),
					item.get('highPriceVolume'),
					item.get('lowPriceVolume')
				)
			]
			timed_item = TimedItem(
				int(item_id),
				price_point
			)
			packaged_items.append(timed_item)


		return packaged_items