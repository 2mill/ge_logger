class LatestItem:

	id: int

	high: int
	low: int

	high_time: int
	low_time: int

	def __init__(
		self,
		id: int,
		high: int,
		low: int,
		high_time: int,
		low_time: int,
	) -> None:
		self.id = id
		self.high = high
		self.low = low

		self.high_time = high_time
		self.low_time = low_time

	def __str__(self) -> str:
		return str(
			{
				'id': self.id,
				'high': self.high,
				'low': self.low,
				'high_time': self.high_time,
				'low_time': self.low_time
			}
		)


# This might be a bad class name... shrug emoji here
class ItemPriceInterval:
	timestamp: int
	avg_high_price: int
	avg_low_price: int
	high_price_volume: int
	low_price_volume: int

	def __init__(
		self,
		timestamp: int,
		avg_high_price: int,
		avg_low_price: int,
		high_price_volume: int,
		low_price_volume: int,
	) -> None:
			self.timestamp = timestamp
			self.avg_high_price = avg_high_price
			self.avg_low_price = avg_low_price
			self.high_price_volume = high_price_volume
			self.low_price_volume = low_price_volume

	def __str__(self) -> str:
		return str({
			'timestamp': self.timestamp,
			'avg_high_price': self.avg_high_price,
			'avg_low_price': self.avg_low_price,
			'high_price_volume': self.high_price_volume,
			'low_price_volume': self.low_price_volume
		})

# This is also a bad class name
class TimedItem:
	id: int
	price_points: list[ItemPriceInterval]
	def __init__(self, id: int,price_points: list[ItemPriceInterval]) -> None:
		self.id = id
		self.price_points=price_points

	def __str__(self) -> str:
		price_points = []
		for data_point in self.price_points:
			# this just looks horrible
			price_points.append(
				{
					'timestamp': data_point.timestamp,
					'avg_high_price':data_point.avg_high_price,
					'avg_low_price': data_point.avg_low_price,
					'high_price_volume': data_point.high_price_volume,
					'low_price_volume': data_point.low_price_volume
				}
			)
		return str({
			'id': self.id,
			'price_points': price_points
		})
class MappedItem:
	id: int
	name: str
	value: int
	examine: str
	members: bool
	low_alch: int
	limit: int
	high_alch: int
	icon: str

	def __init__(self, id: int, name: str, value: int, members: bool, low_alch: int, high_alch: int, limit: int, examine: str, icon: str) -> None:
		self.id = id
		self.name = name
		self.value = value
		self.members = members
		self.low_alch = low_alch
		self.high_alch = high_alch
		self.limit = limit
		self.examine = examine
		self.icon = icon

	def __str__(self) -> str:
		return str({
			'id': self.id,
			'name': self.name,
			'value': self.value,
			'members': self.members,
			'low_alch': self.low_alch,
			'high_alch': self.high_alch,
			'limit': self.limit,
			'examine': self.examine,
			'icon': self.icon
		})

