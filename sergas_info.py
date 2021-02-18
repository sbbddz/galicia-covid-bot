import csv
import requests
import io
import json
import pandas as pd
from datetime import date, timedelta
from lang_module import Lang

lastday = (date.today() - timedelta(2)).strftime("%Y-%m-%d")

class Sergas():
    """
    TODO: Needs refactor and a more fast way for getting data
    """
    def __init__(self):
        self.url = "https://coronavirus.sergas.gal/infodatos/"
        self.mode = "_COVID19_Web_CifrasTotais.csv"
        self.data = self.fetch_data()
        self.lang = Lang().get_lang_file()

    def fetch_data(self, date=lastday):
        response = requests.get(self.url + date + self.mode)
        data = response.text
        return self.parse_data_with_pandas(data)

    def parse_data_with_pandas(self, data):
        buffer = io.StringIO(data)
        parsed_data = pd.read_csv(buffer, sep=',')
        return json.loads(parsed_data.to_json())

    def get_total_cases_lastday(self):
        formatted_string = ""
        for i, j in enumerate(self.data['Casos_Totais'].values()):
            formatted_string += self.lang["total-cases"].format(
                self.get_health_area(str(i)), str(j))

        return formatted_string

    def get_total_cases_day(self, date):
        try:
            data = self.fetch_data(date=date)
        except:
            return self.lang["no-data"]
        formatted_string = ""
        for i, j in enumerate(data['Casos_Totais'].values()):
            formatted_string += self.lang["total-cases"].format(self.get_health_area(str(i)), str(j))
        
        return formatted_string

    def get_health_area(self, number):
        return self.data['Area_Sanitaria'][number]

    def get_last_ten_days(self):
        """
        TODO: Implement method
        """
        pass
