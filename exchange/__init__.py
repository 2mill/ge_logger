import requests
from enum import Enum
from exchange.structs import LatestItem
from exchange.utils import EndpointBuilder
HEADER = {"User-agent": "github.com/2mill/osrs_exchange"}

class Game(Enum):
	OSRS='osrs'
	DeadManMode='dmm'
	FreshStart='fsw'

class Client:
	item_map: dict

	def __init__(self, endpoints=None, source=None, game=None) -> None:
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

	def latest(self, id=None) -> dict:
		endpoint = "/latest"
		if id:
			endpoint += "?id={}".format(id)

		params = {
			'id': id
		}

		res = EndpointBuilder(endpoint, params).fetch()
		data = None
		if res.ok:

			with res.json() as data:
				return data.get('data')
			# data: dict = res.json()
			# data = data.get('data')


		if not data: return []

		return data

	def timeseries(self, id:int, timestep:str) -> list[dict]:

		params = {
			'id': id,
			'timestep': timestep
		}

		res = EndpointBuilder(
			'timeseries',
			params
		).fetch()

		if res.ok:
			return res.json().get('data')

		return [{}]

	def (self, timestep: str) -> dict:
		res = EndpointBuilder(
			timestep
		)

		if res.ok:
			return res.json()


		return {}