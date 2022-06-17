from enum import Enum
import requests as req

HEADER = {
	'User-agent': 'github.com/2mill/osrs_exchange'
}
BASE_URL: str = "https://prices.runescape.wiki/api/v1/osrs"
class Timestep(Enum):
	FIVE_MIN="5m"
	ONE_HOUR="1h"
	SIX_HOURS="6h"


def get_latest(id:int) -> object:
	endpoint = f"{BASE_URL}/latest?id={id}"
	return req.get(endpoint, headers=HEADER)
def get_all_latest() -> object:
	endpoint = f"{BASE_URL}/latest"
	return req.get(endpoint, headers=HEADER)
def get_mapping() -> object:
	endpoint = f"{BASE_URL}/mapping"
	return req.get(endpoint, headers=HEADER)
def get_timestep(timestep: Timestep, id: int) -> object:
	endpoint = f"{BASE_URL}/timeseries?timestep={timestep.value}&id={id}"
	return req.get(endpoint, headers=HEADER)




