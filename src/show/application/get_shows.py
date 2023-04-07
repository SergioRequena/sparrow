from typing import List

from src.show.domain.show import Show
from src.show.infrastructure.shows_repository import ShowsRepository


class GetShows:

    def execute(self, local_shows: List[Show]) -> List[Show]:
        shows = []
        for local_show in local_shows:
            show = ShowsRepository().get_details(str(local_show.id))
            shows.append(show)
        return shows
