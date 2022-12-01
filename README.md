# pyWikiGE

pyWikiGE is a python wrapper for the https://prices.runescape.wiki API.

## Usage

Init the client
```python
  import pyWikiGE
  client = pyWikiGE.Client()
  client.mapping() # Get data from mapping
  client.latest() # Get data from the /latest endpoint
  client.latest(id=4151) # Get data for a specific item id
  client.timeseries(id=4151, timestep='24h') # Get data points for the given interval
  client.timestamp(timestep='5m') # Get average pricing data for items, 5m, 1h, 6h, or 24h ago.
```

This client is still in *beta*, so functionality might not work or might change.
Please report issues, or make PRs for any bug fixes.

# Roadmap

- [ ] Expand testing suite
- [ ] Offline testing
- [ ] Setup file
- [ ] structs testing
- [ ] Push into v1.0 (Karamja)
- [ ] Allow for custom endpoints, or source.
- [ ] Recipe book



# Developed
Developed by Yannick Dorn
https://ydorn.com