from ge import utils
from ge import structs
ITEM_LIST = structs.ItemList()
def test_lookup_all():
	pricing_data = utils.lookup_all(ITEM_LIST)
	assert type(pricing_data) is list

def test_lookup_with_id():
	item_id = 4151
	item = utils.lookup(item_id, ITEM_LIST)
	assert item.id == item_id







	