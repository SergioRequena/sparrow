import json


class JsonDirectoryRepository():

    def execute(self) -> list:
        f = open('tv_shows.json')
        data = json.load(f)
        f.close()
        return data
