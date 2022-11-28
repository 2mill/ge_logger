from exchange import utils

current_url = r'https://prices.runescape.wiki/api/v1/osrs'

def test_endpoint_builder_latest():


	static = {
		'endpoint': 'latest'
	}
	builder = utils.EndpointBuilder(
		static['endpoint']
	)

	assert builder.endpoint == "{}/latest".format(current_url)

def test_endpoint_builder_latest():
	ids = range(5000)
	for id in ids:
		builder = utils.EndpointBuilder(
			'latest',
			params = {
				'id': id
			}
		)

		assert builder.endpoint == "{}/latest?id={}&".format(
			current_url,
			id
		)

def test_endpoint_builder_timestamp():

	endpoints = ['5m', '1h', '6h']

	for endpoint in endpoints:
		assert utils.EndpointBuilder(endpoint).endpoint == '{}/{}'.format(
			current_url,
			endpoint
		)


def test_endpoint_builder_timeseries():
	ids = range(5000)
	timesteps = ['5m', '1h', '6h', '24h']

	for id in ids:
		for timestep in timesteps:
			params = {
				'id': id,
				'timestep': timestep
			}
			endpoint = utils.EndpointBuilder(
				'timeseries',
				params
			)
			assert endpoint.endpoint == "{}/timeseries?id={}&timestep={}&".format(
				current_url,
				id,
				timestep
			)

		

def test_endpoint_builder_mapping():
	
	endpoint = utils.EndpointBuilder(
		'mapping'
	)

	assert endpoint.endpoint == '{}/mapping'.format(
		current_url
	)









