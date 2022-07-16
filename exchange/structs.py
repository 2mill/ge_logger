from typing import Iterable
from ge import endpoints
import json


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


class Item:
    name: str
    id: int
    examine: str
    members: bool
    low_alch: int
    high_alch: int
    limit: int
    value: int  # Still not sure what this is
    pricing: ItemPricingInformation

    def __init__(self, item_information: json.JSONDecoder):
        self.examine = item_information["examine"]
        self.id = item_information["id"]
        self.name = item_information["name"]
        self.members = item_information["members"]
        self.value = item_information["value"]
        # Some items do not have an alch information
        if "lowalch" in item_information.keys():
            self.low_alch = item_information["lowalch"]
            self.high_alch = item_information["highalch"]
        else:
            self.low_alch, self.high_alch = [None, None]
        # Some items don't have limit information
        if "limit" in item_information.keys():
            self.limit = item_information["limit"]
        else:
            self.limit = None


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
