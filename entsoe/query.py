import os
import requests
import arrow
from datetime import datetime
from bs4 import BeautifulSoup as bs
from .params import PARAMS, CONTRACT_MARKET_AGREEMENT_TYPE, AUCTION_TYPE, AUCTION_CATEGORY, PSR_TYPE, PROCESS_TYPE, DOC_STATUS, DOCUMENT_TYPE, BIDDING_ZONE, BIDDING_ZONE_AGGREGATION, CONTROL_AREA, MARKET_BALANCE_AREA

def insertTimeInterval(period, span=None):
    if type(period) is tuple:
        return {
            PARAMS.PERIOD_START: arrow.get(period[0]).to('utc').format('YYYYMMDDHHmm'),
            PARAMS.PERIOD_END: arrow.get(period[1]).to('utc').format('YYYYMMDDHHmm')
        }
    elif (type(period) is datetime) and (type(span) is tuple):
        return {
            PARAMS.PERIOD_START: arrow.get(period).to('utc').shift(hours=span[0]).format('YYYYMMDDHHmm'),
            PARAMS.PERIOD_END: arrow.get(period).to('utc').shift(hours=span[1]).format('YYYYMMDDHHmm')
        }

    raise ValueError('The function need at least one argument between timeInterval and period')

class Query(object):
    def __init__(self, token=os.environ['ENTSOE_TOKEN'], proxy={}):
        self.BASE_URL = 'https://transparency.entsoe.eu/api'
        self.PARAMS = {
            'securityToken': token
        }

    def parseResponse(self, response):
        result = []
        s = bs(response, 'html.parser')
        timeseries = s.find_all('timeseries')
        for timeserie in timeseries:
            timeserieData = {
                'periods': []
            }
            for data in timeserie.findChildren(recursive=False):
                if data.name != 'period':
                    timeserieData[data.name] = data.contents[0]
            for period in timeserie.findChildren('period'):
                periodData = {
                    'points': [],
                    'timeinterval': {}
                }
                for data in period.findChildren(recursive=False):
                    if data.name != 'point' and data.name != 'timeinterval':
                        periodData[data.name] = data.contents[0]
                for data in period.findChild('timeinterval').findChildren():
                    periodData['timeinterval'][data.name] = data.contents[0]
                for entry in period.findChildren('point'):
                    entryData = {}
                    for data in entry.findChildren():
                        entryData[data.name] = data.contents[0]
                    periodData['points'].append(entryData)
                timeserieData['periods'].append(periodData)
            result.append(timeserieData)
        return self.parseDateInterval(result)

    def parseDateInterval(self, parsedResponse):
        for timeserie in parsedResponse:
            for period in timeserie['periods']:
                start = arrow.get(period['timeinterval']['start'])
                end = arrow.get(period['timeinterval']['end'])
                intervals = len(period['points'])
                resolution = (end.timestamp - start.timestamp)/intervals
                for point in period['points']:
                    point['time'] = arrow.get(float(point['position']) * resolution + start.timestamp).isoformat()
        return parsedResponse

    def run(self, params):
        self.PARAMS.update(params)
        res = requests.get(self.BASE_URL, self.PARAMS)
        if res.status_code != 200:
            raise Exception('Can\'t get the data.')
        return self.parseResponse(res.text)

class LoadDomain(Query):
    def actualLoad(self, biddingZone, timeInterval, span=(-24,24)):
        """Get Actual Load
        \nOne year range limit applies
        \nMinimum time interval in query response is one MTU period
        
        Arguments:
            biddingZone {BiddingZone}
            timeInterval {tuple(datetime, datetime) | datetime} -- Delivery time interval From and To. If is datetime, "span" must be used

        Keyword Arguments:
            span {tuple(int, int)} -- Time span for start date and end date
        
        Returns:
            dict -- Parsed response from ENTSOE
        """
        self.query = Query()
        _res = {}
        _res[PARAMS.DOCUMENT_TYPE] =           DOCUMENT_TYPE.SYSTEM_TOTAL_LOAD
        _res[PARAMS.PROCESS_TYPE] =            PROCESS_TYPE.REALISED
        _res[PARAMS.OUT_BIDDINGZONE_DOMAIN] =  biddingZone
        _res.update(insertTimeInterval(timeInterval, span=span))
        return self.query.run(_res)

    def dayAheadLoadForecast(self, biddingZone, timeInterval, span=(-24,24)):
        """Get Day Ahead Total Load Forecast
        \nOne year range limit applies
        \nMinimum time interval in query response is one day
        
        Arguments:
            biddingZone {BiddingZone}
            timeInterval {tuple(datetime, datetime) | datetime} -- Delivery time interval From and To. If is datetime, "span" must be used

        Keyword Arguments:
            span {tuple(int, int)} -- Time span for start date and end date
        
        Returns:
            dict -- Parsed response from ENTSOE
        """
        self.query = Query()
        _res = {}
        _res[PARAMS.DOCUMENT_TYPE] =           DOCUMENT_TYPE.SYSTEM_TOTAL_LOAD
        _res[PARAMS.PROCESS_TYPE] =            PROCESS_TYPE.DAY_AHEAD
        _res[PARAMS.OUT_BIDDINGZONE_DOMAIN] =  biddingZone
        _res.update(insertTimeInterval(timeInterval, span=span))
        return self.query.run(_res)

    def weekAheadLoadForecast(self, biddingZone, timeInterval, span=(-24,24)):
        """Get Week Ahead Total Load Forecast
        \nOne year range limit applies
        \nMinimum time interval in query response is one week
        
        Arguments:
            biddingZone {BiddingZone}
            timeInterval {tuple(datetime, datetime) | datetime} -- Delivery time interval From and To. If is datetime, "span" must be used

        Keyword Arguments:
            span {tuple(int, int)} -- Time span for start date and end date
        
        Returns:
            dict -- Parsed response from ENTSOE
        """
        self.query = Query()
        _res = {}
        _res[PARAMS.DOCUMENT_TYPE] =           DOCUMENT_TYPE.SYSTEM_TOTAL_LOAD
        _res[PARAMS.PROCESS_TYPE] =            PROCESS_TYPE.WEEK_AHEAD
        _res[PARAMS.OUT_BIDDINGZONE_DOMAIN] =  biddingZone
        _res.update(insertTimeInterval(timeInterval, span=span))
        return self.query.run(_res)

    def monthAheadLoadForecast(self, biddingZone, timeInterval, span=(-24,24)):
        """Get Month Ahead Total Load Forecast
        \nOne year range limit applies
        \nMinimum time interval in query response is one month
        
        Arguments:
            biddingZone {BiddingZone}
            timeInterval {tuple(datetime, datetime) | datetime} -- Delivery time interval From and To. If is datetime, "span" must be used

        Keyword Arguments:
            span {tuple(int, int)} -- Time span for start date and end date
        
        Returns:
            dict -- Parsed response from ENTSOE
        """
        self.query = Query()
        _res = {}
        _res[PARAMS.DOCUMENT_TYPE] =           DOCUMENT_TYPE.SYSTEM_TOTAL_LOAD
        _res[PARAMS.PROCESS_TYPE] =            PROCESS_TYPE.MONTH_AHEAD
        _res[PARAMS.OUT_BIDDINGZONE_DOMAIN] =  biddingZone
        _res.update(insertTimeInterval(timeInterval, span=span))
        return self.query.run(_res)

    def yearAheadLoadForecast(self, biddingZone, timeInterval, span=(-24,24)):
        """Get Year Ahead Total Load Forecast
        \nOne year range limit applies
        \nMinimum time interval in query response is one year
        
        Arguments:
            biddingZone {BiddingZone}
            timeInterval {tuple(datetime, datetime) | datetime} -- Delivery time interval From and To. If is datetime, "span" must be used

        Keyword Arguments:
            span {tuple(int, int)} -- Time span for start date and end date
        
        Returns:
            dict -- Parsed response from ENTSOE
        """
        self.query = Query()
        _res = {}
        _res[PARAMS.DOCUMENT_TYPE] =           DOCUMENT_TYPE.SYSTEM_TOTAL_LOAD
        _res[PARAMS.PROCESS_TYPE] =            PROCESS_TYPE.YEAR_AHEAD
        _res[PARAMS.OUT_BIDDINGZONE_DOMAIN] =  biddingZone
        _res.update(insertTimeInterval(timeInterval, span=span))
        return self.query.run(_res)

class TransmissionDomain(Query):
    def forcastedCapacity(self, contractMarketAgreementType, inDomain, outDomain, timeInterval, span=(-24,24)):
        """Get Forcasted Transfer Capacity
        \nOne year range limit applies
        \nMinimum time interval in query response ranges from day to year, depending on selected Contract_MarketAgreement.Type
        
        Arguments:
            contractMarketAgreementType {ContractMarketAgreementType} -- Choose DAILY, WEEKLY, MONTHLY, YEARLY
            inDomain {MarketBalanceArea}
            outDomain {MarketBalanceArea}
            timeInterval {tuple(datetime, datetime) | datetime} -- Delivery time interval From and To. If is datetime, "span" must be used

        Keyword Arguments:
            span {tuple(int, int)} -- Time span for start date and end date
        
        Returns:
            dict -- Parsed response from ENTSOE
        """
        
        self.query = Query()
        _res = {}
        _res[PARAMS.DOCUMENT_TYPE]                    = DOCUMENT_TYPE.ESTIMATED_NET_TRANSFER_CAPACITY
        _res[PARAMS.CONTRACT_MARKET_AGREEMENT_TYPE]   = contractMarketAgreementType
        _res[PARAMS.IN_DOMAIN]                        = inDomain
        _res[PARAMS.OUT_DOMAIN]                       = outDomain
        _res.update(insertTimeInterval(timeInterval, span=span))
        return self.query.run(_res)

    def offeredCapacity(self, auctionType, contractMarketAgreementType, inDomain, outDomain, timeInterval, span=(-24,24), auctionCategory=None):
        """Get Offered Transfer Capacity
        \nOne year range limit applies
        \nMinimum time interval in query response ranges from day to year, depending on selected Contract_MarketAgreement.Type
        
        Arguments:
            auctionType {AuctionType} -- Choose IMPLICIT or EXPLICIT
            contractMarketAgreementType {ContractMarketAgreementType} -- Choose DAILY, WEEKLY, MONTHLY, YEARLY
            inDomain {MarketBalanceArea}
            outDomain {MarketBalanceArea}
            timeInterval {tuple(datetime, datetime) | datetime} -- Delivery time interval From and To. If is datetime, "span" must be used

        Keyword Arguments:
            span {tuple(int, int)} -- Time span for start date and end date
            auctionCategory {AuctionCategory} -- Choose BASE, PEAK, OFF_PEAK, HOURLY (default: None)
        
        Returns:
            dict -- Parsed response from ENTSOE
        """
        
        self.query = Query()
        _res = {}
        _res[PARAMS.DOCUMENT_TYPE]                    = DOCUMENT_TYPE.AGREED_CAPACITY
        _res[PARAMS.AUCTION_TYPE]                     = auctionType
        _res[PARAMS.CONTRACT_MARKET_AGREEMENT_TYPE]   = contractMarketAgreementType
        _res[PARAMS.IN_DOMAIN]                        = inDomain
        _res[PARAMS.OUT_DOMAIN]                       = outDomain
        if auctionCategory:
            _res[PARAMS.AUCTION_CATEGORY]             = auctionCategory
        _res.update(insertTimeInterval(timeInterval, span=span))
        return self.query.run(_res)