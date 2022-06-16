from enum import Enum
import requests as req
base_url: str = "https://prices.runescape.wiki/api/v1/osrs"
class Timestep(Enum):
	FIVE_MIN="5m"
	ONE_HOUR="1h"
	SIX_HOURS="6h"
class Timestamp(Enum):
	FIVE_MIN="5m"
	ONE_HOUR="1h"

def make_req(endpoint_url: str) -> req.Response:
	header = {
		'User-agent': 'github.com/2mill/osrs_exchange'
	}
	return req.get(endpoint_url, header)

latest_all = lambda: make_req(f"{base_url}/latest?")
mapping = lambda: make_req(f"{base_url}/mapping?")
timestamp = lambda time: make_req(f"{base_url}/{time.value}")
timeseries = lambda id, timestep: make_req(f"{base_url}/timeseries?id={id}&timestep={timestep.value}")