from os import times_result
from numpy import identity
import ge.structs as structs
from wikige import structs
import json


# Not trying to accidentally DDOS the wiki here.
mapping_data = json.load(open("./tests/files_for_testing/mapping.json", "r"))

total_items = 0
for item in mapping_data:
    total_items = total_items + 1

lookup_all_data = json.load(open("./tests/files_for_testing/latest.json", "r"))
abyssal_whip_lookup = json.load(
    open("./tests/files_for_testing/latest_aby_whip.json", "r")
)
timeseries = json.load(open("./tests/files_for_testing/timeseries.json", "r"))
timestamp = json.load(open("./tests/files_for_testing/timestamp.json"))
mapping_data = json.load(open("./tests/files_for_testing/mapping.json"))


def test_item_list():
    item_list = structs.ItemList(mapping_data)
    # assert len(item_list.find(4151)) == 1
    assert len(item_list.item_list) == len(mapping_data)


def test_itempricinginformation():
    item = structs.ItemPricingInformation(4151, abyssal_whip_lookup["data"]["4151"])
    assert item.id == 4151


def test_timedpricinginformation_timestamp():
    timed_item = structs.TimedItemPricingInformation(
        4151, timestamp["data"]["4151"], timestamp["timestamp"]
    )
    assert timed_item.id == 4151


def test_timedpricinginformation_timeseries():
    data_timestamp = timeseries["data"][0]["timestamp"]
    timed_item = structs.TimedItemPricingInformation(
        4151, timeseries["data"][0], data_timestamp
    )
    assert timed_item.id == 4151
