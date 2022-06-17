import requests
from ge import endpoints, structs
from ge.endpoints import Timestep
# from ge import endpoints
# from ge.endpoints import Timestep


class WikiGe():
	
	def lookup(self, identifier:int) -> list:
		if type(identifier) is not int and type(identifier) is not str:
			raise ValueError("Lookup only accepts ints or strings")
		if type(identifier) is str:
			item = self.item_list.find_name(identifier)		
			identifier = item.id
		item_pricing_data = endpoints.get_latest(identifier).json()['data']
		return self.item_list.generate_single_item(item_pricing_data)
	def new_lookup(self, identifier:int) -> list:
		if not type(identifier) == int:
			try:
				identifier = int(identifier)
			except ValueError:
				return ValueError
		lookup = endpoints.latest(identifier).json()['data']
		return structs.Item(lookup)

	def lookup_all(self, skip=False) -> list:
		all_pricing_data = endpoints.get_latest_all().json()['data']
		return self.item_list.generate_list(all_pricing_data, skip)
	
	def timeseries(self, identifier, timestep: Timestep):
		if type(identifier) is not int and type(identifier) is not str:
			raise ValueError("Identifier must be string or int")
		if type(identifier) is str:
			# Does not account for none yet.
			item = self.item_list.find(identifier)
			identifier = item.id
		timeseries_data = endpoints.get_timestep(timestep, identifier).json()['data']
		return self.item_list.generate_timestamp_list(timeseries_data, identifier)
