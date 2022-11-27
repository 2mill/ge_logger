from enum import Enum
from json import JSONDecoder
import requests as req

base_url: str = "https://prices.runescape.wiki/api/v1/osrs"


HEADER = {"User-agent": "github.com/2mill/osrs_exchange"}
BASE_URL: str = "https://prices.runescape.wiki/api/v1/osrs"


class Timestep(Enum):
    FIVE_MIN = "5m"
    ONE_HOUR = "1h"
    SIX_HOURS = "6h"


class Timestamp(Enum):
    FIVE_MIN = "5m"
    ONE_HOUR = "1h"


def make_req(endpoint_url: str) -> req.Response:
    header = {"User-agent": "github.com/2mill/osrs_exchange"}
    return req.get(endpoint_url, headers=header)


def Endpoints(Enum):
	LATEST = "/latest"
	LATEST_ALL = "/latest"
	MAPPING = "/mapping"
	TIME="/"



latest = lambda id: make_req(f"{base_url}/latest?id={id}")
latest_all = lambda: make_req(f"{base_url}/latest?")
mapping = lambda: make_req(f"{base_url}/mapping?")
timestamp = lambda time: make_req(f"{base_url}/{time.value}")
timeseries = lambda id, timestep: make_req(
    f"{base_url}/timeseries?id={id}&timestep={timestep.value}"
)


def format_data(data) -> dict:
	if type(data) == dict:
		if "timestamp" in data.keys():
			return data
		try:
			return data["data"]
		except KeyError:
			return data
	return data


def mapping_data() -> dict:
    return format_data(mapping().json())


def latest_data(identity: int) -> dict:
    return format_data(latest(identity).json())


def latest_all_data() -> dict:
    return format_data(latest_all().json())


def timestamp_data(time: Timestamp) -> dict:
    return format_data(timestamp(time).json())


def timeseries(identity: int, timestep: Timestep) -> dict:
    return format_data(timeseries(identity, timestep).json())
