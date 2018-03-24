# python-entsoe
This is a pre-alpha, easy to use python client to consume the ENTSOe rest api.

I took inspiration (though no code was reused) from the awesome [ElectricityMap](http://www.electricitymap.org) project and another attempt to make ENTSOe api useable and useful in python by [EnergieID](https://github.com/EnergieID/entsoe-py).

The client is compatible with **python 2.\*, 3.\*.**

## Basic usage:
To get started clone the project in your working directory and import the `entsoe` module.

    from entsoe.query import Query, LoadDomain, TransmissionDomain
    from entsoe.params import BIDDING_ZONE, PARAMS, CONTRACT_MARKET_AGREEMENT_TYPE, MARKET_BALANCE_AREA, CONTROL_AREA, AUCTION_TYPE
    from datetime import datetime
    
    loadDomain = LoadDomain()
    timeInterval = (
	    datetime(2017,1,1),
	    datetime(2017,1,2)
	)
	
	res0 = loadDomain.actualLoad(
		biddingZone=BIDDING_ZONE.IT_NORTH, timeInterval=timeInterval
	)
	
	transmissionDomain = TransmissionDomain()
	date = datetime(2017,1,1)
	res1 = transmissionDomain.forcastedCapacity(
		contractMarketAgreementType=CONTRACT_MARKET_AGREEMENT_TYPE.DAILY,
		inDomain=BIDDING_ZONE.IT_NORTH_CH,
		outDomain=BIDDING_ZONE.CH,
		timeInterval=date,
		span=(-24,48)
	)
	
	print(res1, res2)