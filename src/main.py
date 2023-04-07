from logging import getLogger

import click

from directory.infrastructure.file.JsonDirectoryRepository import JsonDirectoryRepository
from src.directory.exceptions import DirectoryException

from src.show.application.get_shows import GetShows
from src.show.domain.show import Show

logger = getLogger(__name__)


@click.command()
def main():
    directories = JsonDirectoryRepository().execute()
    shows = []
    for directory in directories:
        try:
            print(repr(directory))
        except DirectoryException as exc:
            logger.error(exc)
    shows_from_api = GetShows().execute(shows)
    print(shows_from_api)


if __name__ == '__main__':
    main()
