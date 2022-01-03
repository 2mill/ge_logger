import ge.tools as tools
from osrsbox import items_api
ITEM_LIST: list = items_api.load()
def test_valid_id():
	abyssal_whip_id: int = 4151
	item_received = tools.get_id(ITEM_LIST, abyssal_whip_id)
	assert item_received.name.lower() == "Abyssal whip".lower()
def test_name():
	"""Test if Given an item name, if it returns a valid item object"""
	abyssal_whip_name: str = "Abyssal Whip"
	item_received = tools.get_id(ITEM_LIST, abyssal_whip_name)
	assert (item_received != None) and item_received.name.lower() == abyssal_whip_name.lower()




