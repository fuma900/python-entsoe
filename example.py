from entsoe.query import Query, LoadDomain, TransmissionDomain
from entsoe.params import BIDDING_ZONE, PARAMS, CONTRACT_MARKET_AGREEMENT_TYPE, MARKET_BALANCE_AREA, CONTROL_AREA, AUCTION_TYPE
from datetime import datetime

loadDomain = LoadDomain()
timeInterval = (
    datetime(2017,1,1),
    datetime(2017,1,2)
)

res0 = loadDomain.actualLoad(BIDDING_ZONE.IT_NORTH, timeInterval=timeInterval)

transmissionDomain = TransmissionDomain()
date = datetime(2017,1,1)

res1 = transmissionDomain.forcastedCapacity(
    contractMarketAgreementType=CONTRACT_MARKET_AGREEMENT_TYPE.DAILY,
    inDomain=BIDDING_ZONE.IT_NORTH_CH,
    outDomain=MARKET_BALANCE_AREA.CH,
    timeInterval=date,
    span=(-24,48)
)
res2 = transmissionDomain.offeredCapacity(
    auctionType=AUCTION_TYPE.EXPLICIT,
    contractMarketAgreementType=CONTRACT_MARKET_AGREEMENT_TYPE.DAILY,
    inDomain=MARKET_BALANCE_AREA.IT,
    outDomain=MARKET_BALANCE_AREA.CH,
    timeInterval=date,
    span=(-24,48)
)

print(res1, res2)