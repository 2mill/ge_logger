from typing import Iterable
from ge import endpoints
from endpoints import Endpoints
import requests
import json


class Client:
	endpoint: Endpoints
	item_map: dict
	BASE_URL = r"https://prices.runescape.wiki/api/v1"

	def __init__(self, endpoints: Endpoints, source=None) -> None:
		if source:
			BASE_URL = source

		res = requests.get(
			"{}/{}",
			self.BASE_URL
			endpoints.MAPPING,
		)

		data: dict = None
		if (res.ok):
			data: dict = res.json()

		self.item_map = {}

		for item in data:

			item: dict = item
			item_id = str(item.get('id'))
			self.item_map[item_id] = item

	def latest(self, id=None) -> list['LatestItem']:
		endpoint = "/latest"
		if id:
			endpoint += "?id={}".format(id)
		res = requests.get(
			"{}/{}".format(
				self.BASE_URL,
				endpoint

			)
		)
		if not res.ok:
			[]
		data: dict = res.json()['data']

		returner = []
		for item_id in data:

			item: dict = data[item]

			returner.append(
				LatestValues(
					item_id,
					item.get('high'),
					item.get('highTime'),
					item.get('low'),
					item.get('lowTime')
				)
			)

	def item(self, item_id: int) -> dict:
		item = self.item_map.get(item_id)
		# Here is where we would pull all the data
		# And filter for the specified ID.

		if not item:
			return {}
		return item


	# since can be 5m, 1h, 6h and 24h
	def timestamp(self, since: str) -> dict:
		url: str = "{}/{}".format(
			self.BASE_URL,
			since
		)

		res = requests.get(url)

		if res.ok: return res.json()
		return {}

	def items(self) -> dict:
		return self.item_map

# TODO Rebuild Item class and allow it as a parameter.


class LatestValues:

	high: int
	low: int
	high_time: int
	low_time: int

	def __init__(self, high: int, high_time: int, low: int, low_time: int) -> None:
		self.high = high
		self.low = low
		self.high_time = high_time
		self.low_time = low_time


class LatestItem:

	id: int

	high: int
	low: int

	high_time: int
	low_time: int

	def __init__(
		self,
		id: int,
		high: int,
		low: int,
		high_time: int,
		low_time: int,
	) -> None:
		self.id = id
		self.high = high
		self.low = low

		self.high_time = high_time
		self.low_time = low_time


class TimestampedItem:
	id: int
	timestamp: int
	avg_high_price: int
	avg_low_price: int
	high_price_volume: int
	low_price_volume: int

	def __init__(
		self,
		id: int,
		avg_high_price: int,
		avg_low_price: int,
		high_price_volume: int,
		low_price_volume: int,
		timestamp: int
		
		) -> None:
			self.id = id
			self.avg_high_price = avg_high_price
			self.avg_low_price = avg_low_price
			self.high_price_volume = high_price_volume
			self.low_price_volume = low_price_volume
			self.timestamp = timestamp


class MappingItem:
	id: int
	name: str
	value: int
	examine: str
	members: bool
	low_alch: int
	limit: int
	high_alch: int
	icon: str

	def __init__(self, id: int, name: str, value: int, members: bool, low_alch: int, high_alch: int, limit: int, examine: str, icon: str) -> None:
		self.id = id
		self.name = name
		self.value = value
		self.members = members
		self.low_alch = low_alch
		self.high_alch = high_alch
		self.limit = limit
		self.examine = examine
		self.icon = icon


class Pricing:
	def __init__(self, pricing_data):
		self.high_price = pricing_data["high"]["price"]
		self.high_time = pricing_data["high"]["time"]
		self.low_price = pricing_data["low"]["price"]
		self.low_time = pricing_data["low"]["time"]


class ItemPricingInformation:
	id: int
	high: int
	high_time: int
	low: int
	lowTime: int

	def __init__(self, identifier: int, pricing_information: json.JSONDecodeError):
		self.id = identifier
		if pricing_information != "{}":
			self.high = pricing_information["high"]
			self.high_time = pricing_information["highTime"]
			self.low = pricing_information["low"]
			self.lowTime = pricing_information["lowTime"]


class TimedItemPricingInformation:
	avg_high_price: int
	avg_low_price: int
	high_volume: int
	low_volume: int
	id: int
	timestamp: int

	def __init__(self, identity, pricing_information, timestamp: int):
		self.id = identity
		self.avg_high_price = pricing_information["avgHighPrice"]
		self.avg_low_price = pricing_information["avgLowPrice"]

		self.high_volume = pricing_information["highPriceVolume"]
		self.low_volume = pricing_information["lowPriceVolume"]

		self.timestamp = timestamp


class ItemList(Iterable):
	def __init__(self, exchange_map: list):
		self.item_list: list[Item] = [
			Item(item_information) for item_information in exchange_map
		]

	def find(self, identifier: int) -> Item:
		"""Finds the item in the list, or returns None if it does not exist"""
		if type(identifier) != int:
			return ValueError
		for item in self.item_list:
			if item.id == identifier:
				return item
		return None

	def __iter__(self) -> Iterable:
		return self.item_list.__iter__()
