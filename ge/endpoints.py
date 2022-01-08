from enum import Enum
import json
import requests as req

from requests.api import request
header = {
	'User-agent': 'github.com/2mill/ge_logger'
}
endpoint: str = "prices.runescape.wiki/api/v1/osrs"
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
def get_latest(id: str) -> Request:
	latest_endpoint: str = find_latest_endpoint(id)
	return req.get(latest_endpoint, headers=header)

def get_mapping() -> Request:
	mapping_endpoint = f"{endpoint}{mapping}"
	return req.get(mapping_endpoint, headers=header)
def get_timestep(id: str, Timestep) -> Request:
	pass


