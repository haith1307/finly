import time
from datetime import datetime

TYPES = [
    "TaxEffectOfUnusualItems",
    "TaxRateForCalcs",
    "NormalizedEBITDA",
    "NormalizedDilutedEPS",
    "NormalizedBasicEPS",
    "TotalUnusualItems",
    "TotalUnusualItemsExcludingGoodwill",
    "NetIncomeFromContinuingOperationNetMinorityInterest",
    "ReconciledDepreciation",
    "ReconciledCostOfRevenue",
    "EBITDA",
    "EBIT",
    "NetInterestIncome",
    "InterestExpense",
    "InterestIncome",
    "ContinuingAndDiscontinuedDilutedEPS",
    "ContinuingAndDiscontinuedBasicEPS",
    "NormalizedIncome",
    "NetIncomeFromContinuingAndDiscontinuedOperation",
    "TotalExpenses",
    "RentExpenseSupplemental",
    "ReportedNormalizedDilutedEPS",
    "ReportedNormalizedBasicEPS",
    "TotalOperatingIncomeAsReported",
    "DividendPerShare",
    "DilutedAverageShares",
    "BasicAverageShares",
    "DilutedEPS",
    "DilutedEPSOtherGainsLosses",
    "TaxLossCarryforwardDilutedEPS",
    "DilutedAccountingChange",
    "DilutedExtraordinary",
    "DilutedDiscontinuousOperations",
    "DilutedContinuousOperations",
    "BasicEPS",
    "BasicEPSOtherGainsLosses",
    "TaxLossCarryforwardBasicEPS",
    "BasicAccountingChange",
    "BasicExtraordinary",
    'OtherunderPreferredStockDividend',
    'NetIncome',
    'OtherTaxes',
    'TotalOtherFinanceCost',
    'SellingAndMarketingExpense',
    'InsuranceAndClaims',
    'NetIncomeExtraordinary',
    'NetIncomeDiscontinuousOperations',
    'GeneralAndAdministrativeExpense',
    'OperatingRevenue',
    'NetNonOperatingInterestIncomeExpense',
    'InterestExpenseNonOperating',
    'OtherNonOperatingIncomeExpenses',
    'BasicContinuousOperations',
    'NetIncomeContinuousOperations',
    'OperatingIncome',
    'Amortization',
    'EarningsFromEquityInterest',
    'SellingGeneralAndAdministration',
    'EarningsFromEquityInterestNetOfTax',
    'DepreciationIncomeStatement',
    'DepletionIncomeStatement',
    'OtherGandA',
    'AmortizationOfIntangiblesIncomeStatement',
    'MinorityInterests',
    'ResearchAndDevelopment',
    'InterestIncomeNonOperating',
    'RestructuringAndMergernAcquisition',
    'GainOnSaleOfPPE',
    'NetIncomeIncludingNoncontrollingInterests',
    'OtherOperatingExpenses',
    'OperatingExpense',
    'ProvisionForDoubtfulAccounts',
    'AverageDilutionEarnings',
    'PreferredStockDividends',
    'ExciseTaxes',
    'SpecialIncomeCharges',
    'ImpairmentOfCapitalAssets',
    'TaxProvision',
    'OtherIncomeExpense',
    'NetIncomeFromTaxLossCarryforward',
    'CostOfRevenue',
    'DepreciationAndAmortizationInIncomeStatement',
    'NetIncomeCommonStockholders',
    'BasicDiscontinuousOperations',
    'DepreciationAmortizationDepletionIncomeStatement',
    'GainOnSaleOfSecurity',
    'TotalRevenue',
    'DilutedNIAvailtoComStockholders',
    'GainOnSaleOfBusiness',
    'OtherSpecialCharges',
    'RentAndLandingFees',
    'GrossProfit',
    'SalariesAndWages',
    'SecuritiesAmortization',
    'PretaxIncome',
    'WriteOff']

QUARTERLY_TYPES = ["quarterly" + t for t in TYPES]
TRAILING_TYPES = ["trailing" + t for t in TYPES]
BASE_LINK = "https://query2.finance.yahoo.com/ws/fundamentals-timeseries/v1/finance/timeseries/"


class YahooFinanceLink:
    def __init__(self, symbol, start_period="493590046", end_period=str(int(time.mktime(datetime.now().timetuple())))):
        self.symbol = symbol
        self.start_period = start_period  # UNIX
        self.end_period = end_period  # UNIX

    def get_link(self):
        quarterly_types = "%2C".join(QUARTERLY_TYPES)
        trailing_types = "%2C".join(TRAILING_TYPES)
        final_link = BASE_LINK + self.symbol + "?lang=en-US&region=US" + f"&symbol={self.symbol}" + \
                     "&padTimeSeries=true" + "&type=" + quarterly_types + trailing_types + "&merge=false" + \
                     f"&period1={self.start_period}" + f"&period2={self.end_period}" + "&corsDomain=finance.yahoo.com"
        return final_link
