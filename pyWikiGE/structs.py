# from endpoints import Endpoints
import requests
import json



# TODO Rebuild Item class and allow it as a parameter.

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


# This might be a bad class name... shrug emoji here
class ItemPriceInterval:
	timestamp: int
	avg_high_price: int
	avg_low_price: int
	high_price_volume: int
	low_price_volume: int

	def __init__(
		self,
		timestamp: int,
		avg_high_price: int,
		avg_low_price: int,
		high_price_volume: int,
		low_price_volume: int,
	) -> None:
			self.timestamp = timestamp
			self.avg_high_price = avg_high_price
			self.avg_low_price = avg_low_price
			self.high_price_volume = high_price_volume
			self.low_price_volume = low_price_volume

class TimedItem:
	id: int

	def __init__(self, id: int,data_points: list[ItemPriceInterval]) -> None:
		self.id = id
	
class MappedItem:
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

