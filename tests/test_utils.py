from ge import utils
from ge import structs
ITEM_LIST = structs.ItemList()
def test_lookup_all():
	print(ITEM_LIST)
	pricing_data = utils.lookup_all(ITEM_LIST)
	assert type(pricing_data) is list





	