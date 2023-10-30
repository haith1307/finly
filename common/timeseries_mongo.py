class TimeseriesMongo:
    def __init__(self, date, metadata, data):
        self.date = date
        self.metadata = metadata
        self.data = data

    def val(self, metadata_field_name="metadata", date_field_name="date", data_field_name="data"):
        return {metadata_field_name: self.metadata, date_field_name: self.date, data_field_name: self.data}
