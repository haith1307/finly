from common.finly_mongo import FinlyMongo
from datetime import date

stock = "GOOGL"
today = date.today.strftime("%Y%m%d")

# Ingest to Finly database
finly_db = FinlyMongo().insert_ts_many_from_json(f"output/{stock}_{today}.json")
