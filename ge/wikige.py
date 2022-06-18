from json import JSONDecoder
import requests
from ge import endpoints, structs
from ge.endpoints import Timestep

# from ge import endpoints
# from ge.endpoints import Timestep
from wikige import endpoints, structs
from wikige.endpoints import Timestep


def lookup_all() -> list:
    item_pricing_information = endpoints.latest_all().json()["data"]
    return [
        structs.ItemPricingInformation(
            int(identity), item_pricing_information[identity]
        )
        for identity in item_pricing_information
    ]


def lookup_id(identity: int) -> structs.ItemPricingInformation:
    if type(identity) != int:
        return ValueError
    item_pricing_information = endpoints.latest(identity).json()["data"]
    if item_pricing_information == "{}":
        return None

    return structs.ItemPricingInformation(
        identity, item_pricing_information[str(identity)]
    )


def mapping() -> structs.ItemList:
    exchange_map = endpoints.mapping().json()
    return structs.ItemList(exchange_map)


def timestamp(
    timestamp: endpoints.Timestamp,
) -> list[structs.TimedItemPricingInformation]:
    item_pricing_information_and_timestamp: JSONDecoder = endpoints.timestamp(
        timestamp
    ).json()
    timestamp = item_pricing_information["timestamp"]
    timestamp, item_pricing_data = [
        item_pricing_information_and_timestamp["timestamp"],
        item_pricing_information_and_timestamp["data"],
    ]
    return [
        structs.TimedItemPricingInformation(
            int(identity), item_pricing_data[identity], timestamp
        )
        for identity in item_pricing_data
    ]


def timeseries(
    identity: int, timestep: endpoints.Timestep
) -> list[structs.TimedItemPricingInformation]:
    item_pricing_data = endpoints.timeseries(identity, timestep).json()
    return [
        structs.TimedItemPricingInformation(identity, data, data["timestamp"])
        for data in item_pricing_data["data"]
    ]


# TODO finish timestep, and implement testing


class WikiGe:
    def lookup(self, identifier: int) -> list:
        if type(identifier) is not int and type(identifier) is not str:
            raise ValueError("Lookup only supports ")
        if type(identifier) is str:
            item = self.item_list.find_name(identifier)
            identifier = item.id
        item_pricing_data = endpoints.get_latest(identifier).json()["data"]
        return self.item_list.generate_single_item(item_pricing_data)

    def new_lookup(self, identifier: int) -> list:
        if not type(identifier) == int:
            try:
                identifier = int(identifier)
            except ValueError:
                return ValueError
        lookup = endpoints.latest(identifier).json()["data"]
        return structs.Item(lookup)

    def lookup_all(self, skip=False) -> list:
        all_pricing_data = endpoints.get_latest_all().json()["data"]
        return self.item_list.generate_list(all_pricing_data, skip)

    def timeseries(self, identifier, timestep: Timestep):
        if type(identifier) is not int and type(identifier) is not str:
            raise ValueError("Identifier must be string or int")
        if type(identifier) is str:
            # Does not account for none yet.
            item = self.item_list.find(identifier)
            identifier = item.id
        timeseries_data = endpoints.get_timestep(timestep, identifier).json()["data"]
        return self.item_list.generate_timestamp_list(timeseries_data, identifier)
