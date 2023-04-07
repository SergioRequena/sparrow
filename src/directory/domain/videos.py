import datetime
import re
from functools import cached_property
from typing import List

from src.directory.exceptions import TmdbIdUnavailableException, InvalidSeasonNumberException, \
    InvalidEpisodeNumberException, InvalidYearException

TMDB_PATTERN = r"\{tmdb-(\d+)\}"
SHOW_NAME_PATTERN = r"(.+) \((\d+)\)"


class Video:
    def __init__(self, path: str, name: str, size: int, mimetype: str, modified_at: datetime.datetime):
        self.path = path
        self.name = name
        self.size = size
        self.mimetype = mimetype
        self.modified_at = modified_at

    @cached_property
    def directory(self) -> str:
        return self.path.split("/")[0]

    @cached_property
    def tmdb_id(self) -> int:
        match = re.findall(TMDB_PATTERN, self.path)
        if not match:
            raise TmdbIdUnavailableException(self.path)
        return int(match[0])

    @cached_property
    def full_show_name(self) -> str:
        """
        Full show name including year.
        :return: show name as string.
        """
        return re.split(TMDB_PATTERN, self.path)[0]

    @cached_property
    def show_name(self) -> str:
        """
        Show name without year
        :return: show name as string.
        """
        return re.findall(SHOW_NAME_PATTERN, self.full_show_name)[0][0]

    @cached_property
    def year(self) -> int:
        """
        Show year
        :return: year as integer
        """
        full_show_name = self.full_show_name
        try:
            return re.findall(SHOW_NAME_PATTERN, self.full_show_name)[0][1]
        except ValueError:
            raise InvalidYearException(full_show_name)

    @cached_property
    def season_episode(self) -> str:
        """
        Season and episode as <season>x<episode>
        :return: season and episode as string
        """
        return self.name.split(" ")[0]

    @cached_property
    def season(self) -> int:
        """
        Season as number
        :return: season number
        """
        season = self.season_episode.split("x")[0]
        try:
            return int(season)
        except ValueError:
            raise InvalidSeasonNumberException(season)

    @cached_property
    def episodes(self) -> List[int]:
        """
        Episodes in the video
        :return: episode numbers as list
        """
        try:
            episodes_range: str = self.season_episode.split("x")[1]
        except IndexError:
            raise InvalidEpisodeNumberException(self.season_episode)
        episodes: List[str] = episodes_range.split("-")
        if len(episodes) > 2:
            raise InvalidEpisodeNumberException(self.season_episode)
        if any(map(lambda x: not x.isdigit(), episodes)):
            raise InvalidEpisodeNumberException(self.season_episode)
        if len(episodes) == 1:
            episodes = [episodes[0]] * 2
        return list(range(int(episodes[0]), int(episodes[1]) + 1))
