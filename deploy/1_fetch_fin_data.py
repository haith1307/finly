from common.api_request import APIRequest
from common.yahoo_finance import YahooFinanceLink
from datetime import date
import json

stock = "GOOGL"
today = date.today().strftime("%Y%m%d")
# Set up API
link = YahooFinanceLink(stock).get_link()

# Request the above API
response = APIRequest().get(link)

# Save to temp output file
with open(f"output/{stock}_{today}.json", "w") as outfile:
    json.dump(response, outfile)
