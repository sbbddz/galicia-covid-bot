from data_parse import Data
from lang_module import Lang

class Sergas():
    def __init__(self):
        self.lang = Lang().get_lang_file()
        self.data = Data()
        self.fetched_data = self.data.fetch_data()
        self.lastday = self.data.lastday

    def get_total_cases_lastday(self):
        formatted_string = self.lang["day-header"].format(self.lastday)
        for i, j in enumerate(self.fetched_data['Casos_Totais'].values()):
            formatted_string += self.lang["total-cases"].format(
                self.data.get_health_area(str(i)), str(j))

        return formatted_string

    def get_total_cases_day(self, date):
        data = self.data.fetch_data(date=date)
        formatted_string = self.lang["day-header"].format(date)
        for i, j in enumerate(data['Casos_Totais'].values()):
            formatted_string += self.lang["total-cases"].format(self.data.get_health_area(i), str(j))
        
        return formatted_string

    def get_new_cases_lastday(self):
        formatted_string = self.lang["day-header"].format(self.lastday)
        for i, j in enumerate(self.fetched_data['Casos_Confirmados_PCR_Ultimas24h'].values()):
            formatted_string += self.lang["new-cases"].format(self.data.get_health_area(i), str(j))
        return formatted_string

