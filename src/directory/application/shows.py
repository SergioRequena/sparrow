from logging import getLogger
from typing import List

import dateutil.parser

from src.directory.domain.paths import Path
from src.directory.domain.shows import Show
from src.directory.domain.videos import Video
from src.directory.exceptions import DirectoryException, TmdbIdUnavailableException

logger = getLogger(__name__)


class Shows:
    def __init__(self, paths: List[Path]):
        self.paths = paths

    def list_shows(self) -> List[Show]:
        shows = {}
        for path in filter(lambda x: not x["IsDir"], self.paths):
            video = Video(
                path["Path"], path["Name"], path["Size"], path["MimeType"], dateutil.parser.parse(path["ModTime"])
            )
            try:
                if video.tmdb_id not in shows:
                    shows[video.tmdb_id] = Show(tmdb_id=video.tmdb_id, name=video.show_name)
                shows[video.tmdb_id].add_video(video)
            except TmdbIdUnavailableException as exc:
                logger.error(exc)
            except DirectoryException as exc:
                logger.error(f"Error {exc} for path {video.path}")
        return list(shows.values())
