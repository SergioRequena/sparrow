from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.directory.domain.shows import Show
    from src.directory.domain.videos import Video


class Season:
    def __init__(self, show: 'Show'):
        self.show = show
        self.videos = set()

    def add_video(self, video: 'Video'):
        self.videos.add(video)

    def __len__(self) -> int:
        return len(self.videos)

    def total_episodes(self):
        return sum(map(lambda video: len(video.episodes), self.videos))
