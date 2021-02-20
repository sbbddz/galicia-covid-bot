import csv
import requests
import io
import json
import pandas as pd
from datetime import date, timedelta


class Data():
    lastday = (date.today() - timedelta(1)).strftime("%Y-%m-%d")

    def __init__(self):
        self.url = "https://coronavirus.sergas.gal/infodatos/"
        self.mode = "_COVID19_Web_CifrasTotais.csv"
        self.data = self.fetch_data()

    def fetch_data(self, date=lastday):
        try:
            response = requests.get(self.url + date + self.mode)
            data = response.text
            return self.parse_data_with_pandas(data)
        except:
            return "No data avaliable"

    def parse_data_with_pandas(self, data):
        buffer = io.StringIO(data)
        parsed_data = pd.read_csv(buffer, sep=',')
        return json.loads(parsed_data.to_json())

    def get_health_area(self, number):
        return self.data['Area_Sanitaria'][str(number)]