import requests
import json
import os
from dotenv import load_dotenv

from src.show.domain.Season import Season
from src.show.domain.Show import Show

load_dotenv()
URL = 'https://api.themoviedb.org/3/'
API_KEY = os.getenv('TMDB_API_KEY')


class ShowsRepository:

    def get_details(self, show_id: str) -> Show:
        url = f'{URL}tv/{show_id}'
        response = self.__get(url)
        seasons = []
        for season in response['seasons']:
            seasons.append(Season(
                number=season['season_number'],
                episode_count=season['episode_count'],
            ))
        return Show(
            id=response['id'],
            name=response['name'],
            seasons=seasons,
        )

    def __get(self, url: str):
        payload = {'api_key': API_KEY, 'language': 'en-EN'}
        response = requests.get(
            url,
            params=payload,
            headers={'User-Agent': 'Custom'}
        )
        if 200 == response.status_code:
            return json.loads(response.text)
        else:
            return None
