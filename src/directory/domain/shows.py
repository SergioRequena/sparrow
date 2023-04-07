from typing import Iterator

from src.directory.domain.seasons import Season
from src.directory.domain.videos import Video


class Show:
    def __init__(self, tmdb_id: int, name: str):
        self.tmdb_id = tmdb_id
        self.name = name
        self.seasons_by_number = {}

    def add_video(self, video: Video) -> None:
        if video.season not in self.seasons_by_number:
            self.seasons_by_number[video.season] = Season(self)
        self.seasons_by_number[video.season].add_video(video)

    def total_episodes(self) -> int:
        return sum(map(lambda season: season.total_episodes(), list(self)))

    def __len__(self):
        return len(self.seasons_by_number)

    def __iter__(self) -> Iterator[Season]:
        yield from self.seasons_by_number.values()

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"<Show {self.name} ({len(self)} seasons & {self.total_episodes()} episodes)>"
