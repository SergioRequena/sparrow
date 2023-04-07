

class DirectoryException(Exception):
    pass


class TmdbIdUnavailableException(DirectoryException):
    def __init__(self, path: str):
        self.path = path
        super().__init__(f"TMDB id unavailable in path {path}")


class InvalidSeasonNumberException(DirectoryException):
    def __init__(self, season: str):
        self.season = season
        super().__init__(f"Season number {season} is invalid (this is not a number)")


class InvalidEpisodeNumberException(DirectoryException):
    def __init__(self, season: str):
        self.season = season
        super().__init__(f"Episode number {season} is invalid")


class InvalidYearException(DirectoryException):
    def __init__(self, name):
        self.name = name
        super().__init__(f"Invalid year in {name} show name")
