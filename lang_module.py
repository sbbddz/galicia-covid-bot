import json
from datetime import datetime


class Lang():

    def __init__(self):
        with open("lang.json", "r") as file:
            self.lang = json.loads(file.read())

    def get_lang_file(self):
        return self.lang

    @staticmethod
    def parse_date_eu(date):
        return datetime.strptime(
            date, "%Y-%m-%d").strftime("%d-%m-%Y")

    @staticmethod
    def parse_date_us(date):
        return datetime.strptime(
            date, "%d-%m-%Y").strftime("%Y-%m-%d")
