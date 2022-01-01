from ge.tools import get_id
import osrsbox
def test_invalid_id():
	abyssal_whip_id: int= 4151
	item_received = get_id([4151], abyssal_whip_id)
	assert item_received.name == "Abyssal Whip"




