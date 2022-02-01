from enum import Enum
import requests as req

header = {
	'User-agent': 'github.com/2mill/osrs_exchange'
}
endpoint: str = "https://prices.runescape.wiki/api/v1/osrs"
latest, timeseries, mapping = [f"{endpoint}/latest/", f"{endpoint}/mapping/", f"{endpoint}/mapping/"]
class Timestep(Enum):
	FIVE_MIN="5m"
	ONE_HOUR="1h"
	SIX_HOURS="6h"


def get_latest(id=-1) -> object:
	if id == -1:  return req.get(latest, headers=header)
	return req.get(
		f"{latest}?id={id}",
		headers=header
	)

def get_latest_all() -> object:
	return req.get(latest_endpoint, headers=header)

def get_mapping() -> object:
	mapping_endpoint = f"{endpoint}{mapping}"
	return req.get(mapping_endpoint, headers=header)
def get_timestep(id: str, timestep: Timestep) -> object:
	if id is None or timestep is None: return None
	timestep_endpoint = f"{timeseries}?timestep={timestep}&id={id}"
	return req.get(timestep_endpoint, headers=header)




