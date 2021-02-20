import json

class Lang():

    def __init__(self):
        with open("lang.json", "r") as file:
            self.lang = json.loads(file.read())

    def get_lang_file(self):
        return self.lang
