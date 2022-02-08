from enum import Enum
import requests as req

header = {
	'User-agent': 'github.com/2mill/osrs_exchange'
}
base_url: str = "https://prices.runescape.wiki/api/v1/osrs"
class Timestep(Enum):
	FIVE_MIN="5m"
	ONE_HOUR="1h"
	SIX_HOURS="6h"


def get_latest(id:int) -> object:
	endpoint = f"{base_url}/latest?id={id}"
	return req.get(endpoint, headers=header)

def get_latest_all() -> object:
	endpoint = f"{base_url}/latest"
	return req.get(endpoint, headers=header)


def get_mapping() -> object:
	endpoint = f"{base_url}/mapping"
	return req.get(endpoint, headers=header)
def get_timestep(timestep: Timestep, id: int) -> object:
	endpoint = f"{base_url}/timeseries?timestep={timestep.value}&id={id}"
	return req.get(endpoint, headers=header)




