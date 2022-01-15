import re
from ge.endpoints import get_latest, get_mapping, get_timestep
import structs
import json

def lookup(identifier, item_list) -> object:
	item = item_list.find(identifier)
	pricing = reformat(item.id, get_latest(item.id).json())
	return structs.PricedItem(item, pricing)

def lookup_all(item_list) -> list:
	items = get_latest(None).json()['data']
	pricing_list = []
	pass




def update(item) -> object:
	# Make a new item object with the most recent price for it.
	return lookup(item.id)

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
