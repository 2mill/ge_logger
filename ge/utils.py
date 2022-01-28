import re
from ge.endpoints import get_latest, get_mapping, get_timestep
from ge import structs
import json

def lookup(identifier, item_list) -> object:
	item = item_list.find(identifier)
	item_pricing_json = get_latest(item.id).json()
	pricing = reformat(item.id, item_pricing_json)
	return structs.PricedItem(item, pricing)

def lookup_all(item_list) -> list:
	all_items_pricing_json:list= get_latest().json()['data']

	pricing_list = []
	# the raw data is formatted with id first. 
	items = 0
	not_found = 0
	for identifier in all_items_pricing_json:
		items = items + 1	

		# OSRSBOX DB and Wiki can be out of date.
		# Figure out how this problem should be handled.
		item = item_list.find(int(identifier))

		if item is None:
			not_found = not_found + 1
			print(item_list)
			print(int(identifier))
			print(item)
			print(f"{items} {not_found}")

		

		# This needs to be here for the reformater.
		# item_pricing_json = {
		# 	identifier:all_items_pricing_json[identifier]
		# }
		# pricing = reformat(identifier, item_pricing_json)
		# item = item_list.find(int(identifier))
		# priced_item = structs.PricedItem(pricing,item)
		# pricing_list.append(priced_item)
	# return pricing_list	





def update(item) -> object:
	pass

def reformat(id:int, pricing_data: json) -> dict:
	"""
		Reformatting item data to be friendlier for structs.Pricing
	"""
	return {
		'high': {
			'price': pricing_data[id]['high'],
			'time': pricing_data[id]['highTime']
		},
		'low': {
			'price': pricing_data[id]['low'],
			'time': pricing_data[id]['lowTime']
		}
	}
