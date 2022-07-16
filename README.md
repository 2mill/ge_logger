#osrs_exchange
osrs_exchange is a python wrapper for [Oldschool Runescape Wiki Grand Exchange Data API](https://prices.runescape.wiki/osrs/). Learn more about the project [here](https://oldschool.runescape.wiki/w/RuneScape:Real-time_Prices)

I have developed this tool on and off for a year. Therefore, the possiblity for bugs and errors to occur are prevelent.

I do not plan on maintaining this project further or adding many more features. This code is free for you to fork and do with as desired.

If there are any issues, please make sure to write an issue.

## Usage

`import exchange` will import the necessary functions.

`exchange.latest_all()` will return every recent item's price as an object called ItemPricingInformation.

`exchange.latest_id(*id*)` will return the most recent pricing data for the given item ID.
`exchange.mapping()` will return the mapping data formatted as an ItemList object.

`exchange.timestamp(exchange.Timestamp)` will return the all of the item pricing information from that given timestamp as a list of ItemPricingInformation.

`exchange.timestamp(*id*, exchange.Timestep)` will return the prices, in the given interval, as a list of TimeItemPricingInformation data objects.

## Enums for Timeseries & Timestamp

While it is possible to pass literal values into Timestep and Timestamp arguments, there are enums to make this easier.

`exchange.Timestamp` includes options for `FIVE_MIN` and `ONE_HOUR`.

`exchange.Timestep` includes options for `FIVE_MIN`, `ONE_HOUR`, and `SIX_HOURS`.

## Structs
### ItemPricingInformation
`ItemPricingInformation.id` will return an integer of Item's ID.

`ItemPricingInformation.high` will return the Item's high price.

`ItemPricingInformation.low` will return the Item's low price.

`ItemPricingInformation.high_time` will return the Item's high time.

`ItemPricingInformation.low` will return the Item's low time.

### TimedItemPricingInformation
`avg_high_price` and `avg_low_price` returns an integer value of the item's high or low price.

`high_volume` nad `low_volume` returns an integer of the volume traded for that item during the timestep.

`timestamp` is the timestamp of the data's recording.

`id` is also included.

### Item
`Item.name` is the name of the item.

`Item.id` is the integer ID of the item.

`Item.examine` is the examin text for the item.

`Item.memebers` is a boolean value and indicates if the item is members only.

`Item.limit` gives item exchange trading limit, None if there is no trading limit.

#### Alching
`low_alch` and `high_alch` will give low and high alch values IF the items are alchable. Otherwise None will be returned.

### ItemList
`ItemList.find(*id*)` will return an Item from the list if the ID matches. Throws ValueError if non int is passed as an argument. Returns None if not found.
The ItemList is iterable.





##Usage
I still need to work on proper interface imports and more testing needs to be done so use at your own risk.
`import ge.wikige` will import the correct package.
Afterwards, initialize the ge with `ge.wikige.WikiGe()`.
Further documentation will be provided soon.

## Testing Files
The files you'd want to use to use pytest can be found [here](https://www.mediafire.com/folder/jgydulp1rmcl3/files_for_testing).

Then run: `mkdir tests/files_for_testing` and copy the files into this directory.



