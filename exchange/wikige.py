import requests
from ge import endpoints, structs
from ge.endpoints import Timestep, Timestamp


def lookup_all() -> list:
    item_pricing_information = endpoints.latest_all_data()
    return [
        structs.ItemPricingInformation(
            int(identity), item_pricing_information[identity]
        )
        for identity in item_pricing_information
    ]


def lookup_id(identity: int) -> structs.ItemPricingInformation:
    if type(identity) != int:
        return ValueError
    item_pricing_information = endpoints.latest_data(identity)
    if item_pricing_information == "{}":
        return None

    return structs.ItemPricingInformation(
        identity, item_pricing_information[str(identity)]
    )


def mapping() -> structs.ItemList:
    exchange_map = endpoints.mapping_data()
    return structs.ItemList(exchange_map)


def timestamp(
    identity: int,
    timestamp: endpoints.Timestamp,
) -> list[structs.TimedItemPricingInformation]:
    item_pricing_information_and_timestamp: dict = endpoints.timestamp_data(
        identity, timestamp
    )
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




