from datetime import date

import pymongo

from common.api_request import APIRequest
from common.finly_mongo import FinlyMongo
from common.yahoo_finance import YahooFinanceLink
import json


if __name__ == '__main__':
    stock = "MSFT"
    today = date.today().strftime("%Y%m%d")

    """Step 1"""
    # Set up API
    link = YahooFinanceLink(stock).get_link()

    # Request the above API
    response = APIRequest().get(link)

    # Save to temp output file
    with open(f"output/{stock}_{today}.json", "w") as outfile:
        json.dump(response, outfile)

    """Step 2"""
    finly_db = FinlyMongo(is_atlas=True)
    finly_db.insert_ts_many_from_json(f"output/{stock}_{today}.json")

    # # for obj in finly.db['financialData'].find({'metadata.symbol': 'GOOGL', 'metadata.type': 'quarterlyOperatingExpense'}):
    # #     print(obj)
    # for obj in finly.db['financialData'].find({"metadata.symbol": 'GOOGL', 'metadata.type': 'quarterlyNetIncome'}, sort=[('date', -1)]):
    #     print(obj)


