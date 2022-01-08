from enum import Enum
import json
import requests as req

header = {
	'User-agent': 'github.com/2mill/ge_logger'
}
endpoint: str = "https://prices.runescape.wiki/api/v1/osrs"
latest: str = "/latest"
timeseries: str  = "/timeseries"
mapping: str = "/mapping"
class Timestep(Enum):
	FIVE_MIN="5m"
	ONE_HOUR="1h"
	SIX_HOURS="6h"


def find_latest_endpoint(id: str) -> str:
	return_endpoint = f"{endpoint}{latest}"
	if id is None:
		return return_endpoint
	else:
		return f"{return_endpoint}?id={id}"
def get_latest(id: str) -> object:
	latest_endpoint: str = find_latest_endpoint(id)
	return req.get(latest_endpoint, headers=header)

def get_mapping() -> object:
	mapping_endpoint = f"{endpoint}{mapping}"
	return req.get(mapping_endpoint, headers=header)
def get_timestep(id: str, timestep: Timestep) -> object:
	if id is None or timestep is None: return None
	timestep_endpoint = f"{endpoint}{timeseries}?timestep={timestep}&id={id}"
	return req.get(timestep_endpoint, headers=header)




