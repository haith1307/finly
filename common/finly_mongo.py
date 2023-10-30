from pymongo import MongoClient
from common.timeseries_mongo import TimeseriesMongo
import json
from datetime import datetime


class FinlyMongo:
    def __init__(self, server="localhost", port=27017):
        self.client = MongoClient(server, port)
        self.db = self.client.finly

    def create_ts_collection(self, collection_name, date_field="date", meta_field="metadata"):
        self.db.create_collection(collection_name, timeseries={'timeField': date_field, 'metaField': meta_field})

    def insert_ts_one(self, ts_data: TimeseriesMongo, collection_name="financialData"):
        self.db[collection_name].insert_one(ts_data.val())

    def insert_ts_many(self, ts_data_lst, collection_name="financialData"):
        self.db[collection_name].insert_many([ts_data.val() for ts_data in ts_data_lst])

    def insert_ts_many_from_json(self, filename):

        # Read from step 1 output json
        with open(filename, 'r') as openfile:
            json_object = json.load(openfile)

        # Process output json to get list of records
        results = json_object['timeseries']['result']
        ts_data_lst = []
        for result in results:
            symbol = result['meta']['symbol'][0]
            type = result['meta']['type'][0]

            timestamps = result.get('timestamp')
            records = result.get(type)
            if timestamps is not None and records is not None and len(timestamps) == len(records):
                # if there is result
                for i in range(len(records)):
                    if records[i] is not None:
                        t = TimeseriesMongo(metadata={'symbol': symbol, 'type': type},
                                        date=datetime.fromtimestamp(int(timestamps[i])),
                                        data={'currencyCode': records[i]['currencyCode'],
                                              'raw': records[i]['reportedValue']['raw']}
                                        )
                        ts_data_lst.append(t)

        # Ingest to Finly database
        self.insert_ts_many(ts_data_lst)
