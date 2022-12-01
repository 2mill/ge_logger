from enum import Enum
from json import JSONDecoder
import requests
BASE_URL: str = "https://prices.runescape.wiki/api/v1/osrs"

constants = {
	'BASE_URL': r'https://prices.runescape.wiki/api/v1/osrs'
}


def get(base_url: str, endpoint: str) -> requests.Response:
	pass


def endpoint_builder(endpoint: str, params:dict, base_url=None, user_agent:str=None) -> str:
	pass




class EndpointBuilder:

	IFS = r'&'
	QUERY = r'?'
	base_url = r'https://prices.runescape.wiki/api/v1/osrs'
	headers =  {
		'User-Agent': r'github.com/2mill/osrs_exchange'
	}
	def __init__(self, endpoint: str, params:dict=None, base_url=None, user_agent=None) -> None:


		if base_url:
			self.base_url = base_url


		self.endpoint = "{}/{}".format(
			self.base_url,
			endpoint
		)


		if params:
			self.endpoint += self.QUERY
			for param in params:
				self.endpoint += "{}={}{}".format(
					param,
					params.get(param),
					self.IFS
				)
			


		self.params = params
		if user_agent: user_agent = user_agent
	def fetch(self) -> requests.Response:
		return requests.get(
			self.endpoint,
			headers=self.headers
		)

		

	
	