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

'''

"4.1.1. Actual Total Load [6.1.A]"                                      [ IMPLEMENTED ]
"4.1.2. Day-Ahead Total Load Forecast [6.1.B]"                          [ IMPLEMENTED ]
"4.1.3. Week-Ahead Total Load Forecast [6.1.C]"                         [ IMPLEMENTED ]
"4.1.4. Month-Ahead Total Load Forecast [6.1.D]"                        [ IMPLEMENTED ]
"4.1.5. Year-Ahead Total Load Forecast [6.1.E]"                         [ IMPLEMENTED ]
"4.1.6. Year-Ahead Forecast Margin [8.1]"
"4.2.1. Expansion and Dismantling Projects [9.1]"
"4.2.2. Forecasted Capacity [11.1.A]"                                   [ IMPLEMENTED ]
"4.2.3. Offered Capacity [11.1.A]"                                      [ IMPLEMENTED ]
"4.2.4. Flow-based Parameters [11.1.B]"                                 [ TO DO ]
"4.2.5. Intraday Transfer Limits [11.3]"
"4.2.6. Explicit Allocation Information (Capacity) [12.1.A]"            [ TO DO ]
"4.2.7. Explicit Allocation Information (Revenue only) [12.1.A]"        [ TO DO ]
"4.2.8. Total Capacity Nominated [12.1.B]"                              [ TO DO ]
"4.2.9. Total Capacity Already Allocated [12.1.C]"                      [ TO DO ]
"4.2.10. Day Ahead Prices [12.1.D]"                                     [ TO DO ]
"4.2.11. Implicit Auction — Net Positions [12.1.E]"
"4.2.12. Implicit Auction — Congestion Income [12.1.E]"
"4.2.13. Total Commercial Schedules [12.1.F]"
"4.2.14. Day-ahead Commercial Schedules [12.1.F]"                       [ TO DO ]
"4.2.15. Physical Flows [12.1.G]"                                       [ TO DO ]
"4.2.16. Capacity Allocated Outside EU [12.1.H]"
"4.3.1. Redispatching [13.1.A]"
"4.3.2. Countertrading [13.1.B]"
"4.3.3. Costs of Congestion Management [13.1.C]"
"4.4.1. Installed Generation Capacity Aggregated [14.1.A]"
"4.4.2. Installed Generation Capacity per Unit [14.1.B]"
"4.4.3. Day-ahead Aggregated Generation [14.1.C]"
"4.4.4. Day-ahead Generation Forecasts for Wind and Solar [14.1.D]"
"4.4.5. Current Generation Forecasts for Wind and Solar [14.1.D]"
"4.4.6. Intraday Generation Forecasts for Wind and Solar [14.1.D]"
"4.4.7. Actual Generation Output per Generation Unit [16.1.A]"
"4.4.8. Aggregated Generation per Type [16.1.B&C]"
"4.4.9. Aggregated Filling Rate of Water Reservoirs and Hydro Storage Plants [16.1.D]"
"4.5.1. Production and Generation Units"
"4.6.1. Amount of Balancing Reserves Under Contract [17.1.B]"
"4.6.2. Prices of Procured Balancing Reserves [17.1.C]"
"4.6.3. Accepted Aggregated Offers [17.1.D]"
"4.6.4. Activated Balancing Energy [17.1.E]"
"4.6.5. Prices of Activated Balancing Energy [17.1.F]"
"4.6.6. Imbalance Prices [17.1.G]"
"4.6.7. Total Imbalance Volumes [17.1.H]"
"4.6.8. Financial Expenses and Income for Balancing [17.1.I]"
"4.6.9. Cross-border Balancing [17.1.J]"
"4.7.1. Unavailability of Consumption Units [7.1A&B]"
"4.7.2. Unavailability of Transmission Infrastructure [10.1.A&B]"
"4.7.3. Unavailability of Offshore Grid Infrastructure [10.1.C]"
"4.7.4. Unavailability of Generation Units [15.1.A&B]"
"4.7.5. Unavailability of Production Units [15.1.C&D]"

'''