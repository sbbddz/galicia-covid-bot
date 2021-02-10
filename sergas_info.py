import csv
import requests
import io
import json
import pandas as pd
from datetime import date, timedelta


class Sergas():
    """
    TODO: Needs refactor
    """

    yesterday = (date.today() - timedelta(1)).strftime("%Y-%m-%d")

    def __init__(self):
        self.url = "https://coronavirus.sergas.gal/infodatos/"
        self.mode = "_COVID19_Web_CifrasTotais.csv"

    def get_full_data(self, date=yesterday):
        response = requests.get(self.url + date + self.mode)
        data = response.text
        return self.parse_data_with_pandas(data)

    def get_total_cases(self, date):
        """
        TODO: Too slow getting info, maybe one requests instead of 9000? hosting the file in the server?
        """
        data = self.get_full_data(date)['Casos_Totais']
        formatted_string = ""
        for i, j in enumerate(data.values()):
            formatted_string += "En la " + self.get_health_area(str(i)) + " hay " + \
                str(j) + " casos totales\n"

        return formatted_string

    def get_health_area(self, number):
        return self.get_full_data()['Area_Sanitaria'][number]

    def parse_data_with_pandas(self, data):
        buffer = io.StringIO(data)
        parsed_data = pd.read_csv(buffer, sep=',')
        return json.loads(parsed_data.to_json())
