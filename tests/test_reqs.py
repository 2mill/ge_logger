import ge.tools as tools
from osrsbox import items_api
def test_invalid_id():
	abyssal_whip_id: str = "4151"
	all_db_items = items_api.load()
	item_received = tools.get_id(all_db_items, abyssal_whip_id)
	assert item_received.name.lower() == "Abyssal whip".lower()
def test_name():
	"""Test if Given an item name, if it returns a valid item object"""
	pass;




