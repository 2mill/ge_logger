from wikige import endpoints

# def test_timeseries():
# 	timestep = endpoints.Timestep.FIVE_MIN.value
# 	res = endpoints.get_timestep("4151", timestep)
# 	assert res.status_code == 200 


def test_mapping():
	assert endpoints.get_mapping().status_code == 200
def test_timestep_enum():
	timesteps = endpoints.Timestep
	steps = [timesteps.FIVE_MIN.value, timesteps.ONE_HOUR.value, timesteps.SIX_HOURS.value]
	assert ['5m', '1h', '6h'] == steps
def test_timestep():
	assert endpoints.get_timestep(endpoints.Timestep.FIVE_MIN, 4151).status_code == 200
	
	


