# python-entsoe
This is an easy to use python client to consume the ENTSOe rest api.

I took inspiration (though no code was reused) from the awesome [ElectricityMap](http://www.electricitymap.org) project and another attempt to make ENTSOe api useable and useful in python by [EnergieID](https://github.com/EnergieID/entsoe-py).

The client is compatible with **python 2.\*, 3.\*.**

Please note that the client is still in **pre-alpha** and in active development.

## Basic usage:
To get started clone the project in your working directory and import the `entsoe` module.

    from datetime import datetime
    from entsoe.query import LoadDomain, TransmissionDomain
    from entsoe.params import AUCTION_TYPE, BIDDING_ZONE, CONTRACT_MARKET_AGREEMENT_TYPE, CONTROL_AREA, MARKET_BALANCE_AREA
    
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

Which results in an output similar to the following

    [
        {
            "periods": [{
                "points": [
                    {
                        "position": "1",
                        "quantity": "3016",
                        "time": "2016-12-31T00:00:00+00:00"
                    },
                    ...
                    {
                        "position": "24",
                        "quantity": "3016",
                        "time": "2016-12-31T23:00:00+00:00"
                    },
                ],
                "timeinterval": {
                    "start": "2016-12-30T23:00Z",
                    "end": "2016-12-31T23:00Z"
                },
                "resolution": "PT60M"
            }],
            "mrid": "1",
            "businesstype": "A27",
            "in_domain.mrid": "10Y1001A1001A68B",
            "out_domain.mrid": "10YCH-SWISSGRIDZ",
            "quantity_measure_unit.name": "MAW",
            "curvetype": "A01"
        },
        ...
    ]