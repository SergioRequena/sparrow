import json

from src.directory.application.shows import Shows


class JsonDirectoryRepository():

    def execute(self) -> list:
        f = open('tv_shows.json')
        data = json.load(f)
        f.close()
        return Shows(data).list_shows()
