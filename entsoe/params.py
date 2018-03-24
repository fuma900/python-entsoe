#!/usr/bin/python3

class Helper(object):
    def __init__(self):
        pass
    
    def getParamFromValue(self, value):
        for var in vars(self).keys():
            if not callable(getattr(self, var)):
                if getattr(self, var) == value:
                    return var
        return None

class Params(Helper):
    def __init__(self):
        super()
        self.DOCUMENT_TYPE = 'DocumentType'
        self.DOC_STATUS = 'DocStatus'
        self.PROCESS_TYPE = 'ProcessType'
        self.BUSINESS_TYPE = 'BusinessType'
        self.PSR_TYPE = 'PsrType'
        self.MARKET_AGREEMENT_TYPE = 'Type_MarketAgreement.Type'
        self.CONTRACT_MARKET_AGREEMENT_TYPE = 'Contract_MarketAgreement.Type'
        self.AUCTION_TYPE = 'Auction.Type'
        self.AUCTION_CATEGORY = 'Auction.Category'
        self.CLASSIFICATION_SEQUENCE_ATTRIBUTE_INSTANCE_COMPONENT_POSITION = 'ClassificationSequence_AttributeInstanceComponent.Position'
        self.OUT_BIDDINGZONE_DOMAIN = 'OutBiddingZone_Domain'
        self.BIDDING_ZONE_DOMAIN = 'BiddingZone_Domain'
        self.CONTROL_AREA_DOMAIN = 'ControlArea_Domain'
        self.IN_DOMAIN = 'In_Domain'
        self.OUT_DOMAIN = 'Out_Domain'
        self.ACQUIRING_DOMAIN = 'Acquiring_Domain'
        self.CONNECTING_DOMAIN = 'Connecting_Domain'
        self.REGISTERED_RESOURCE = 'RegisteredResource'
        self.TIME_INTERVAL = 'TimeInterval'
        self.PERIOD_START = 'PeriodStart'
        self.PERIOD_END = 'PeriodEnd'
        self.TIME_INTERVAL_UPDATE = 'TimeIntervalUpdate'
        self.PERIOD_START_UPDATE = 'PeriodStartUpdate'
        self.PERIOD_END_UPDATE = 'PeriodEndUpdate'

class ContractMarketAgreementType(Helper):
    def __init__(self):
        super()
        self.DAILY = 'A01'
        self.WEEKLY = 'A02'
        self.MONTHLY = 'A03'
        self.YEARLY = 'A04'
        self.TOTAL = 'A05'
        self.LONG_TERM = 'A06'
        self.INTRADAY = 'A07'
        self.HOURLY = 'A13'

class AuctionType(Helper):
    def __init__(self):
        super()
        self.IMPLICIT = 'A01'
        self.EXPLICIT = 'A02'

class AuctionCategory(Helper):
    def __init__(self):
        super()
        self.BASE = 'A01'
        self.PEAK = 'A02'
        self.OFF_PEAK = 'A03'
        self.HOURLY = 'A04'

class PsrType(Helper):
    def __init__(self):
        super()
        self.MIXED = 'A03'
        self.GENERATION = 'A04'
        self.LOAD = 'A05'
        self.BIOMASS = 'B01'
        self.FOSSIL_BROWN_COAL_LIGNITE = 'B02'
        self.FOSSIL_COAL_DERIVED_GAS = 'B03'
        self.FOSSIL_GAS = 'B04'
        self.FOSSIL_HARD_COAL = 'B05'
        self.FOSSIL_OIL = 'B06'
        self.FOSSIL_OIL_SHALE = 'B07'
        self.FOSSIL_PEAT = 'B08'
        self.GEOTHERMAL = 'B09'
        self.HYDRO_PUMPED_STORAGE = 'B10'
        self.HYDRO_RUN_OF_RIVER_AND_POUNDAGE = 'B11'
        self.HYDRO_WATER_RESERVOIR = 'B12'
        self.MARINE = 'B13'
        self.NUCLEAR = 'B14'
        self.OTHER_RENEWABLE = 'B15'
        self.SOLAR = 'B16'
        self.WASTE = 'B17'
        self.WIND_OFFSHORE = 'B18'
        self.WIND_ONSHORE = 'B19'
        self.OTHER = 'B20'
        self.AC_LINK = 'B21'
        self.DC_LINK = 'B22'
        self.SUBSTATION = 'B23'
        self.TRANSFORMER = 'B24'

class BusinessType(Helper):
    def __init__(self):
        super()
        self.ALREADY_ALLOCATED_CAPACITY = 'A29'
        self.REQUESTED_CAPACITY = 'A43'
        self.SYSTEM_OPERATOR_REDISPATCHING = 'A46'
        self.PLANNED_MAINTENANCE = 'A53'
        self.UNPLANNED_OUTAGE = 'A54'
        self.INTERNAL_REDISPATCH = 'A85'
        self.FREQUENCY_CONTAINMENT_RESERVE = 'A95'
        self.AUTOMATIC_FREQUENCY_RESTORATION_RESERVE = 'A96'
        self.MANUAL_FREQUENCY_RESTORATION_RESERVE = 'A97'
        self.REPLACEMENT_RESERVE = 'A98'
        self.INTERCONNECTOR_NETWORK_EVOLUTION = 'B01'
        self.INTERCONNECTOR_NETWORK_DISMANTLING = 'B02'
        self.COUNTER_TRADE = 'B03'
        self.CONGESTION_COSTS = 'B04'
        self.CAPACITY_ALLOCATED = 'B05'
        self.AUCTION_REVENUE = 'B07'
        self.TOTAL_NOMINATED_CAPACITY = 'B08'
        self.NET_POSITION = 'B09'
        self.CONGESTION_INCOME = 'B10'
        self.PRODUCTION_UNIT = 'B11'

class ProcessType(Helper):
    def __init__(self):
        super()
        self.DAY_AHEAD = 'A01'
        self.INTRA_DAY_INCREMENTAL = 'A02'
        self.REALISED = 'A16'
        self.INTRADAY_TOTAL = 'A18'
        self.WEEK_AHEAD = 'A31'
        self.MONTH_AHEAD = 'A32'
        self.YEAR_AHEAD = 'A33'
        self.SYNCHRONISATION_PROCESS = 'A39'
        self.INTRADAY_PROCESS = 'A40'

class DocStatus(Helper):
    def __init__(self):
        super()
        self.ACTIVE = 'A05'
        self.CANCELLED = 'A09'
    
class DocumentType(Helper):
    def __init__(self):
        super()
        self.FINALISED_SCHEDULE = 'A09'
        self.AGGREGATED_ENERGY_DATA_REPORT = 'A11'
        self.ALLOCATION_RESULT_DOCUMENT = 'A25'
        self.CAPACITY_DOCUMENT = 'A26'
        self.AGREED_CAPACITY = 'A31'
        self.PRICE_DOCUMENT = 'A44'
        self.ESTIMATED_NET_TRANSFER_CAPACITY = 'A61'
        self.REDISPATCH_NOTICE = 'A63'
        self.SYSTEM_TOTAL_LOAD = 'A65'
        self.INSTALLED_GENERATION_PER_TYPE = 'A68'
        self.WIND_AND_SOLAR_FORECAST = 'A69'
        self.LOAD_FORECAST_MARGIN = 'A70'
        self.GENERATION_FORECAST = 'A71'
        self.RESERVOIR_FILLING_INFORMATION = 'A72'
        self.ACTUAL_GENERATION = 'A73'
        self.WIND_AND_SOLAR_GENERATION = 'A74'
        self.ACTUAL_GENERATION_PER_TYPE = 'A75'
        self.LOAD_UNAVAILABILITY = 'A76'
        self.PRODUCTION_UNAVAILABILITY = 'A77'
        self.TRANSMISSION_UNAVAILABILITY = 'A78'
        self.OFFSHORE_GRID_INFRASTRUCTURE_UNAVAILABILITY = 'A79'
        self.GENERATION_UNAVAILABILITY = 'A80'
        self.CONTRACTED_RESERVES = 'A81'
        self.ACCEPTED_OFFERS = 'A82'
        self.ACTIVATED_BALANCING_QUANTITIES = 'A83'
        self.ACTIVATED_BALANCING_PRICES = 'A84'
        self.IMBALANCE_PRICES = 'A85'
        self.IMBALANCE_VOLUME = 'A86'
        self.FINANCIAL_SITUATION = 'A87'
        self.CROSS_BORDER_BALANCING = 'A88'
        self.CONTRACTED_RESERVE_PRICES = 'A89'
        self.INTERCONNECTION_NETWORK_EXPANSION = 'A90'
        self.COUNTER_TRADE_NOTICE = 'A91'
        self.CONGESTION_COSTS = 'A92'
        self.DC_LINK_CAPACITY = 'A93'
        self.NON_EU_ALLOCATIONS = 'A94'
        self.CONFIGURATION_DOCUMENT = 'A95'
        self.FLOW_BASED_ALLOCATIONS = 'B11'

class BiddingZone(Helper):
    def __init__(self):
        super()
        self.DE_50HERTZ = '10YDE-VE-------2'
        self.ALB = '10YAL-KESH-----5'
        self.BY = '10Y1001A1001A51S'
        self.BE = '10YBE----------2'
        self.BA = '10YBA-JPCC-----D'
        self.BG = '10YCA-BULGARIA-R'
        self.CZ_DE_SK = '10YDOM-CZ-DE-SKK'
        self.HR = '10YHR-HEP------M'
        self.CY = '10YCY-1001A0003J'
        self.CZ = '10YCZ-CEPS-----N'
        self.AT_DE_LU = '10Y1001A1001A63L'
        self.DK1 = '10YDK-1--------W'
        self.DK2 = '10YDK-2--------M'
        self.EE = '10Y1001A1001A39I'
        self.FI = '10YFI-1--------U'
        self.MK = '10YMK-MEPSO----8'
        self.FR = '10YFR-RTE------C'
        self.GR = '10YGR-HTSO-----Y'
        self.HU = '10YHU-MAVIR----U'
        self.IE = '10Y1001A1001A59C'
        self.IT_BRINDISI = '10Y1001A1001A699'
        self.IT_CENTRE_NORTH = '10Y1001A1001A70O'
        self.IT_CENTRE_SOUTH = '10Y1001A1001A71M'
        self.IT_FOGGIA = '10Y1001A1001A72K'
        self.IT_GR = '10Y1001A1001A66F'
        self.IT_MALTA = '10Y1001A1001A877'
        self.IT_NORTH = '10Y1001A1001A73I'
        self.IT_NORTH_AT = '10Y1001A1001A80L'
        self.IT_NORTH_CH = '10Y1001A1001A68B'
        self.IT_NORTH_FR = '10Y1001A1001A81J'
        self.IT_NORTH_SI = '10Y1001A1001A67D'
        self.IT_PRIOLO = '10Y1001A1001A76C'
        self.IT_ROSSANO = '10Y1001A1001A77A'
        self.IT_SARDINIA = '10Y1001A1001A74G'
        self.IT_SICILY = '10Y1001A1001A75E'
        self.IT_SOUTH = '10Y1001A1001A788'
        self.RU_KALININGRAD = '10Y1001A1001A50U'
        self.LV = '10YLV-1001A00074'
        self.LT = '10YLT-1001A0008Q'
        self.MT = '10Y1001A1001A93C'
        self.ME = '10YCS-CG-TSO---S'
        self.GB = '10YGB----------A'
        self.NL = '10YNL----------L'
        self.NO1 = '10YNO-1--------2'
        self.NO2 = '10YNO-2--------T'
        self.NO3 = '10YNO-3--------J'
        self.NO4 = '10YNO-4--------9'
        self.NO5 = '10Y1001A1001A48H'
        self.CZ_PL = '10YDOM-1001A082L'
        self.PL = '10YPL-AREA-----S'
        self.PT = '10YPT-REN------W'
        self.MD = '10Y1001A1001A990'
        self.RO = '10YRO-TEL------P'
        self.RU = '10Y1001A1001A49F'
        self.SE1 = '10Y1001A1001A44P'
        self.SE2 = '10Y1001A1001A45N'
        self.SE3 = '10Y1001A1001A46L'
        self.SE4 = '10Y1001A1001A47J'
        self.RS = '10YCS-SERBIATSOV'
        self.SK = '10YSK-SEPS-----K'
        self.SI = '10YSI-ELES-----O'
        self.ES = '10YES-REE------0'
        self.CH = '10YCH-SWISSGRIDZ'
        self.TR = '10YTR-TEIAS----W'
        self.UK = '10Y1001C--00003F'

    def getParamFromValue(self, value):
        for var in vars(self).keys():
            if not callable(getattr(self, var)):
                if getattr(self, var) == value:
                    return var
        return None
    

class BiddingZoneAggregation(Helper):
    def __init__(self):
        super()
        self.DE_50HERTZ = '10YDE-VE-------2'
        self.CZ_DE_SK = '10YDOM-CZ-DE-SKK'
        self.CZ_PL = '10YDOM-1001A082L'
        self.PL = '10YPL-AREA-----S'

class ControlArea(Helper):
    def __init__(self):
        super()
        self.DE_50HERTZ = '10YDE-VE-------2'
        self.ALB = '10YAL-KESH-----5'
        self.DE_AMP = '10YDE-RWENET---I'
        self.AT = '10YAT-APG------L'
        self.BY = '10Y1001A1001A51S'
        self.BE = '10YBE----------2'
        self.BA = '10YBA-JPCC-----D'
        self.BG = '10YCA-BULGARIA-R'
        self.HR = '10YHR-HEP------M'
        self.CY = '10YCY-1001A0003J'
        self.CZ = '10YCZ-CEPS-----N'
        self.DK = '10Y1001A1001A796'
        self.EE = '10Y1001A1001A39I'
        self.FI = '10YFI-1--------U'
        self.MK = '10YMK-MEPSO----8'
        self.FR = '10YFR-RTE------C'
        self.GR = '10YGR-HTSO-----Y'
        self.HU = '10YHU-MAVIR----U'
        self.IE = '10YIE-1001A00010'
        self.IT = '10YIT-GRTN-----B'
        self.RU_KALININGRAD = '10Y1001A1001A50U'
        self.LV = '10YLV-1001A00074'
        self.LT = '10YLT-1001A0008Q'
        self.LU = '10YLU-CEGEDEL-NQ'
        self.MT = '10Y1001A1001A93C'
        self.ME = '10YCS-CG-TSO---S'
        self.GB = '10YGB----------A'
        self.NL = '10YNL----------L'
        self.NO = '10YNO-0--------C'
        self.CZ_PL = '10YDOM-1001A082L'
        self.PL = '10YPL-AREA-----S'
        self.PT = '10YPT-REN------W'
        self.MD = '10Y1001A1001A990'
        self.RO = '10YRO-TEL------P'
        self.RU = '10Y1001A1001A49F'
        self.RS = '10YCS-SERBIATSOV'
        self.SK = '10YSK-SEPS-----K'
        self.SI = '10YSI-ELES-----O'
        self.GB_NORTHERN_IRELAND = '10Y1001A1001A016'
        self.ES = '10YES-REE------0'
        self.SE = '10YSE-1--------K'
        self.CH = '10YCH-SWISSGRIDZ'
        self.DE_TENNET = '10YDE-EON------1'
        self.DE_TRANSNET = '10YDE-ENBW-----N'
        self.TR = '10YTR-TEIAS----W'
        self.UK_DOBTPP = '10Y1001A1001A869'
        self.UK_BEI = '10YUA-WEPS-----0'
        self.UK_IPS = '10Y1001C--000182'

class MarketBalanceArea(Helper):
    def __init__(self):
        super()
        self.ALB = '10YAL-KESH-----5'
        self.AT = '10YAT-APG------L'
        self.BY = '10Y1001A1001A51S'
        self.BE = '10YBE----------2'
        self.BA = '10YBA-JPCC-----D'
        self.BG = '10YCA-BULGARIA-R'
        self.HR = '10YHR-HEP------M'
        self.CY = '10YCY-1001A0003J'
        self.CZ = '10YCZ-CEPS-----N'
        self.DE_LU = '10Y1001A1001A82H'
        self.DK1 = '10YDK-1--------W'
        self.DK2 = '10YDK-2--------M'
        self.EE = '10Y1001A1001A39I'
        self.FI = '10YFI-1--------U'
        self.MK = '10YMK-MEPSO----8'
        self.FR = '10YFR-RTE------C'
        self.GR = '10YGR-HTSO-----Y'
        self.HU = '10YHU-MAVIR----U'
        self.IE = '10Y1001A1001A59C'
        self.IT = '10YIT-GRTN-----B'
        self.IT_MACROZONE_NORTH = '10Y1001A1001A84D'
        self.IT_MACROZONE_SOUTH = '10Y1001A1001A85B'
        self.RU_KALININGRAD = '10Y1001A1001A50U'
        self.LV = '10YLV-1001A00074'
        self.LT = '10YLT-1001A0008Q'
        self.MT = '10Y1001A1001A93C'
        self.ME = '10YCS-CG-TSO---S'
        self.GB = '10YGB----------A'
        self.NL = '10YNL----------L'
        self.NO1 = '10YNO-1--------2'
        self.NO2 = '10YNO-2--------T'
        self.NO3 = '10YNO-3--------J'
        self.NO4 = '10YNO-4--------9'
        self.NO5 = '10Y1001A1001A48H'
        self.NO = '10YNO-0--------C'
        self.PL = '10YPL-AREA-----S'
        self.PT = '10YPT-REN------W'
        self.MD = '10Y1001A1001A990'
        self.RO = '10YRO-TEL------P'
        self.RU = '10Y1001A1001A49F'
        self.SE1 = '10Y1001A1001A44P'
        self.SE2 = '10Y1001A1001A45N'
        self.SE3 = '10Y1001A1001A46L'
        self.SE4 = '10Y1001A1001A47J'
        self.RS = '10YCS-SERBIATSOV'
        self.SK = '10YSK-SEPS-----K'
        self.SI = '10YSI-ELES-----O'
        self.ES = '10YES-REE------0'
        self.SE = '10YSE-1--------K'
        self.CH = '10YCH-SWISSGRIDZ'
        self.TR = '10YTR-TEIAS----W'
        self.UK = '10Y1001C--00003F'

PARAMS = Params()
CONTRACT_MARKET_AGREEMENT_TYPE = ContractMarketAgreementType()
AUCTION_TYPE = AuctionType()
AUCTION_CATEGORY = AuctionCategory()
PSR_TYPE = PsrType()
PROCESS_TYPE = ProcessType()
DOC_STATUS = DocStatus()
DOCUMENT_TYPE = DocumentType()
BIDDING_ZONE = BiddingZone()
BIDDING_ZONE_AGGREGATION = BiddingZoneAggregation()
CONTROL_AREA = ControlArea()
MARKET_BALANCE_AREA = MarketBalanceArea()